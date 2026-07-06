const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');

/**
 * POST /api/quiz/generate
 * Body: { topic: string, numQuestions: number, difficulty: 'easy'|'medium'|'hard' }
 * Returns: { questions: [{id, question, options, answer, explanation}] }
 */
router.post('/generate', async (req, res) => {
  const { topic, numQuestions = 5, difficulty = 'medium' } = req.body;

  if (!topic || topic.trim() === '') {
    return res.status(400).json({ error: 'Topic is required.' });
  }

  const count = Math.min(Math.max(parseInt(numQuestions) || 5, 1), 15);

  try {
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
    res.json(result);
  } catch (error) {
    console.error('Quiz generate error:', error.message);
    res.status(500).json({ error: 'Failed to generate quiz. Please try again.' });
  }
});

module.exports = router;
