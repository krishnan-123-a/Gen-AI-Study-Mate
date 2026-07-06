const express = require('express');
const router = express.Router();
const { openai, MODEL } = require('../config/openai');
const ChatHistory = require('../models/ChatHistory');
const { isDemoMode, getMockChatReply } = require('../utils/mockResponses');

/**
 * POST /api/chat
 * Body: { message, history, sessionId }
 * Returns: { reply, sessionId }
 */
router.post('/', async (req, res) => {
  const { message, history = [], sessionId } = req.body;

  if (!message || message.trim() === '') {
    return res.status(400).json({ error: 'Message is required.' });
  }

  try {
    let reply;

    if (isDemoMode()) {
      // Demo mode — return rich mock reply instantly
      await new Promise((r) => setTimeout(r, 600)); // small delay for realism
      reply = getMockChatReply(message);
    } else {
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
        ...history.slice(-10),
        { role: 'user', content: message },
      ];

      const completion = await openai.chat.completions.create({
        model: MODEL,
        messages,
        temperature: 0.7,
        max_tokens: 1024,
      });
      reply = completion.choices[0].message.content;
    }

    // Persist to MongoDB
    const sid = sessionId || `session_${Date.now()}`;
    const newMessages = [
      ...history,
      { role: 'user', content: message },
      { role: 'assistant', content: reply },
    ];

    await ChatHistory.findOneAndUpdate(
      { sessionId: sid },
      { sessionId: sid, messages: newMessages },
      { upsert: true, new: true }
    );

    res.json({ reply, sessionId: sid });
  } catch (error) {
    console.error('Chat error:', error.message);
    res.status(500).json({ error: 'Failed to get a response. Please try again.' });
  }
});

/**
 * GET /api/chat/history
 */
router.get('/history', async (req, res) => {
  try {
    const sessions = await ChatHistory.find()
      .sort({ updatedAt: -1 })
      .limit(10)
      .select('sessionId messages updatedAt');
    res.json({ sessions });
  } catch (error) {
    console.error('Chat history error:', error.message);
    res.status(500).json({ error: 'Failed to fetch chat history.' });
  }
});

/**
 * GET /api/chat/session/:sessionId
 */
router.get('/session/:sessionId', async (req, res) => {
  try {
    const session = await ChatHistory.findOne({ sessionId: req.params.sessionId });
    if (!session) return res.status(404).json({ error: 'Session not found.' });
    res.json({ messages: session.messages });
  } catch (error) {
    console.error('Session fetch error:', error.message);
    res.status(500).json({ error: 'Failed to fetch session.' });
  }
});

/**
 * DELETE /api/chat/session/:sessionId
 */
router.delete('/session/:sessionId', async (req, res) => {
  try {
    await ChatHistory.deleteOne({ sessionId: req.params.sessionId });
    res.json({ success: true });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete session.' });
  }
});

module.exports = router;
