const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');

/**
 * POST /api/topics/explain
 * Body: { topic: string, level: 'beginner' | 'intermediate' | 'advanced' }
 * Returns: { explanation: string, prerequisites: string[], nextTopics: string[] }
 */
router.post('/explain', async (req, res) => {
  const { topic, level = 'beginner' } = req.body;

  if (!topic || topic.trim() === '') {
    return res.status(400).json({ error: 'Topic is required.' });
  }

  try {
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

    const result = JSON.parse(completion.choices[0].message.content);
    res.json(result);
  } catch (error) {
    console.error('Topic explain error:', error.message);
    res.status(500).json({ error: 'Failed to explain topic. Please try again.' });
  }
});

/**
 * POST /api/topics/summary
 * Body: { text: string }
 * Returns: { summary: string }
 */
router.post('/summary', async (req, res) => {
  const { text } = req.body;

  if (!text || text.trim() === '') {
    return res.status(400).json({ error: 'Text is required.' });
  }

  try {
    const completion = await openai.chat.completions.create({
      model: MODEL,
      messages: [
        {
          role: 'user',
          content: `Summarize the following text in clear, concise bullet points suitable for studying:\n\n${text}`,
        },
      ],
      temperature: 0.4,
      max_tokens: 512,
    });

    res.json({ summary: completion.choices[0].message.content });
  } catch (error) {
    console.error('Summary error:', error.message);
    res.status(500).json({ error: 'Failed to generate summary. Please try again.' });
  }
});

module.exports = router;
