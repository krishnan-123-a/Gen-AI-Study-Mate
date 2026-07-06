const express = require('express');
const router = express.Router();
const { isDemoMode } = require('../utils/mockResponses');
const mongoose = require('mongoose');

router.get('/', (req, res) => {
  res.json({
    status: 'OK',
    demoMode: isDemoMode(),
    db: mongoose.connection.readyState === 1 ? 'connected' : 'disconnected',
    message: isDemoMode()
      ? 'Running in DEMO mode — add a real OPENAI_API_KEY in .env for live AI responses'
      : 'Running with live OpenAI API',
  });
});

module.exports = router;
