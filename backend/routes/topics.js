const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');
const { isDemoMode, getMockTopicExplanation } = require('../utils/mockResponses');

/**
 * POST /api/topics/explain
 * Body: { topic, level }
 */
router.post('/explain', async (req, res) => {
  const { topic, level = 'beginner' } = req.body;

  if (!topic || topic.trim() === '') {
    return res.status(400).json({ error: 'Topic is required.' });
  }

  try {
    let result;

    if (isDemoMode()) {
      await new Promise((r) => setTimeout(r, 700));
      result = getMockTopicExplanation(topic, level);
    } else {
      const prompt = `Explain the topic "${topic}" for a ${level} level student.
Respond ONLY with valid JSON in this exact format:
{
  "explanation": "Clear, thorough explanation of the topic",
  "keyPoints": ["point 1", "point 2", "point 3"],
  "prerequisites": ["prerequisite topic 1", "prerequisite topic 2"],
  "nextTopics": ["next topic 1", "next topic 2"],
  "realWorldExample": "A practical real-world example"
}`;

      const completion = await openai.chat.completions.create({
        model: MODEL,
        messages: [{ role: 'user', content: prompt }],
        temperature: 0.5,
        max_tokens: 1024,
        response_format: { type: 'json_object' },
      });
      result = JSON.parse(completion.choices[0].message.content);
    }

    res.json(result);
  } catch (error) {
    console.error('Topic explain error:', error.message);
    res.status(500).json({ error: 'Failed to explain topic. Please try again.' });
  }
});

/**
 * POST /api/topics/summary
 * Body: { text }
 */
router.post('/summary', async (req, res) => {
  const { text } = req.body;

  if (!text || text.trim() === '') {
    return res.status(400).json({ error: 'Text is required.' });
  }

  try {
    let summary;

    if (isDemoMode()) {
      await new Promise((r) => setTimeout(r, 500));
      const sentences = text.split(/[.!?]+/).filter(Boolean).slice(0, 5);
      summary = sentences.map((s) => `• ${s.trim()}`).join('\n') ||
        '• This text covers foundational concepts\n• Key ideas are clearly presented\n• Practical applications are highlighted';
    } else {
      const completion = await openai.chat.completions.create({
        model: MODEL,
        messages: [{
          role: 'user',
          content: `Summarize the following text in clear, concise bullet points suitable for studying:\n\n${text}`,
        }],
        temperature: 0.4,
        max_tokens: 512,
      });
      summary = completion.choices[0].message.content;
    }

    res.json({ summary });
  } catch (error) {
    console.error('Summary error:', error.message);
    res.status(500).json({ error: 'Failed to generate summary. Please try again.' });
  }
});

module.exports = router;
