const mongoose = require('mongoose');

const questionSchema = new mongoose.Schema({
  id:          { type: Number, required: true },
  question:    { type: String, required: true },
  options:     [String],
  answer:      { type: String, required: true },
  explanation: String,
  userAnswer:  String,
  correct:     Boolean,
}, { _id: false });

const quizResultSchema = new mongoose.Schema({
  topic:       { type: String, required: true },
  difficulty:  { type: String, enum: ['easy', 'medium', 'hard'], default: 'medium' },
  questions:   [questionSchema],
  score:       { type: Number, required: true },
  total:       { type: Number, required: true },
  percentage:  { type: Number, required: true },
}, { timestamps: true });

module.exports = mongoose.model('QuizResult', quizResultSchema);
