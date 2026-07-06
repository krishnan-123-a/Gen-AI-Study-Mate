const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');
const FlashcardSet = require('../models/FlashcardSet');

/**
 * POST /api/flashcards/generate
 * Body: { topic, numCards }
 * Generates flashcards via AI and saves to MongoDB
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

    // Auto-save to MongoDB
    const saved = await FlashcardSet.create({
      topic,
      flashcards: result.flashcards,
      numCards: result.flashcards.length,
    });

    res.json({ ...result, setId: saved._id });
  } catch (error) {
    console.error('Flashcard generate error:', error.message);
    res.status(500).json({ error: 'Failed to generate flashcards. Please try again.' });
  }
});

/**
 * GET /api/flashcards/history
 * Returns last 10 saved flashcard sets
 */
router.get('/history', async (req, res) => {
  try {
    const sets = await FlashcardSet.find()
      .sort({ createdAt: -1 })
      .limit(10)
      .select('topic numCards createdAt _id');
    res.json({ sets });
  } catch (error) {
    console.error('Flashcard history error:', error.message);
    res.status(500).json({ error: 'Failed to fetch flashcard history.' });
  }
});

/**
 * GET /api/flashcards/:id
 * Returns a saved flashcard set by ID
 */
router.get('/:id', async (req, res) => {
  try {
    const set = await FlashcardSet.findById(req.params.id);
    if (!set) return res.status(404).json({ error: 'Flashcard set not found.' });
    res.json(set);
  } catch (error) {
    console.error('Flashcard fetch error:', error.message);
    res.status(500).json({ error: 'Failed to fetch flashcard set.' });
  }
});

/**
 * DELETE /api/flashcards/:id
 */
router.delete('/:id', async (req, res) => {
  try {
    await FlashcardSet.findByIdAndDelete(req.params.id);
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete flashcard set.' });
  }
});

module.exports = router;
