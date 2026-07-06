const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');
const QuizResult = require('../models/QuizResult');
const { isDemoMode, getMockQuiz } = require('../utils/mockResponses');

/**
 * POST /api/quiz/generate
 * Body: { topic, numQuestions, difficulty }
 */
router.post('/generate', async (req, res) => {
  const { topic, numQuestions = 5, difficulty = 'medium' } = req.body;

  if (!topic || topic.trim() === '') {
    return res.status(400).json({ error: 'Topic is required.' });
  }

  const count = Math.min(Math.max(parseInt(numQuestions) || 5, 1), 15);

  try {
    let questions;

    if (isDemoMode()) {
      await new Promise((r) => setTimeout(r, 800));
      questions = getMockQuiz(topic, count, difficulty);
    } else {
      const prompt = `Generate ${count} multiple-choice quiz questions about "${topic}" at ${difficulty} difficulty.
Respond ONLY with valid JSON in this exact format:
{
  "questions": [
    {
      "id": 1,
      "question": "Question text here?",
      "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
      "answer": "A) Option 1",
      "explanation": "Why this answer is correct"
    }
  ]
}`;

      const completion = await openai.chat.completions.create({
        model: MODEL,
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.7,
        max_tokens: 2048,
        response_format: { type: 'json_object' },
      });
      const result = JSON.parse(completion.choices[0].message.content);
      questions = result.questions;
    }

    res.json({ questions });
  } catch (error) {
    console.error('Quiz generate error:', error.message);
    res.status(500).json({ error: 'Failed to generate quiz. Please try again.' });
  }
});

/**
 * POST /api/quiz/save
 */
router.post('/save', async (req, res) => {
  const { topic, difficulty, questions, score, total } = req.body;

  if (!topic || !questions || score === undefined || !total) {
    return res.status(400).json({ error: 'Missing required fields.' });
  }

  try {
    const quizResult = await QuizResult.create({
      topic,
      difficulty: difficulty || 'medium',
      questions,
      score,
      total,
      percentage: Math.round((score / total) * 100),
    });
    res.json({ success: true, id: quizResult._id });
  } catch (error) {
    console.error('Quiz save error:', error.message);
    res.status(500).json({ error: 'Failed to save quiz result.' });
  }
});

/**
 * GET /api/quiz/history
 */
router.get('/history', async (req, res) => {
  try {
    const results = await QuizResult.find()
      .sort({ createdAt: -1 })
      .limit(10)
      .select('topic difficulty score total percentage createdAt');
    res.json({ results });
  } catch (error) {
    console.error('Quiz history error:', error.message);
    res.status(500).json({ error: 'Failed to fetch quiz history.' });
  }
});

module.exports = router;
