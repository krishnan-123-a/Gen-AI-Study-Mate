const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');

/**
 * POST /api/flashcards/generate
 * Body: { topic: string, numCards: number }
 * Returns: { flashcards: [{id, front, back}] }
 */
router.post('/generate', async (req, res) => {
  const { topic, numCards = 10 } = req.body;

  if (!topic || topic.trim() === '') {
    return res.status(400).json({ error: 'Topic is required.' });
  }

  const count = Math.min(Math.max(parseInt(numCards) || 10, 1), 20);

  try {
    const prompt = `Create ${count} study flashcards for the topic "${topic}".
Each flashcard should have a clear question or term on the front and a concise answer or definition on the back.
Respond ONLY with valid JSON in this exact format:
{
  "flashcards": [
    {
      "id": 1,
      "front": "Question or term",
      "back": "Answer or definition"
    }
  ]
}`;

    const completion = await openai.chat.completions.create({
      model: MODEL,
      messages: [{ role: 'user', content: prompt }],
      temperature: 0.6,
      max_tokens: 1500,
      response_format: { type: 'json_object' },
    });

    const result = JSON.parse(completion.choices[0].message.content);
    res.json(result);
  } catch (error) {
    console.error('Flashcard generate error:', error.message);
    res.status(500).json({ error: 'Failed to generate flashcards. Please try again.' });
  }
});

module.exports = router;
