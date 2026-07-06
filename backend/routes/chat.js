const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');

/**
 * POST /api/chat
 * Body: { message: string, history: [{role, content}] }
 * Returns: { reply: string }
 */
router.post('/', async (req, res) => {
  const { message, history = [] } = req.body;

  if (!message || message.trim() === '') {
    return res.status(400).json({ error: 'Message is required.' });
  }

  try {
    const messages = [
      {
        role: 'system',
        content: `You are Gen-AI Study Mate, an intelligent and friendly AI tutor.
Your goal is to help students understand complex topics clearly and concisely.
- Break down difficult concepts into simple explanations.
- Use examples and analogies where helpful.
- Encourage curiosity and deeper learning.
- If asked for a quiz, generate relevant questions.
- Always be supportive and patient.`,
      },
      ...history.slice(-10), // keep last 10 messages for context
      { role: 'user', content: message },
    ];

    const completion = await openai.chat.completions.create({
      model: MODEL,
      messages,
      temperature: 0.7,
      max_tokens: 1024,
    });

    const reply = completion.choices[0].message.content;
    res.json({ reply });
  } catch (error) {
    console.error('Chat error:', error.message);
    res.status(500).json({ error: 'Failed to get a response. Please try again.' });
  }
});

module.exports = router;
