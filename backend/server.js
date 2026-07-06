const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');
const path = require('path');
const connectDB = require('./config/db');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Connect to MongoDB
connectDB();

// Middleware
app.use(cors());
app.use(express.json());

// Routes
const chatRoutes      = require('./routes/chat');
const topicRoutes     = require('./routes/topics');
const quizRoutes      = require('./routes/quiz');
const flashcardRoutes = require('./routes/flashcards');

app.use('/api/chat',       chatRoutes);
app.use('/api/topics',     topicRoutes);
app.use('/api/quiz',       quizRoutes);
app.use('/api/flashcards', flashcardRoutes);

// Serve React frontend in production
if (process.env.NODE_ENV === 'production') {
  app.use(express.static(path.join(__dirname, '../frontend/build')));
  app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend/build', 'index.html'));
  });
}

// Health check
app.get('/api/health', (req, res) => {
  const mongoose = require('mongoose');
  res.json({
    status: 'OK',
    message: 'Gen-AI Study Mate API is running',
    db: mongoose.connection.readyState === 1 ? 'connected' : 'disconnected',
  });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

module.exports = app;
