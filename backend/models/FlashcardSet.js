const mongoose = require('mongoose');

const cardSchema = new mongoose.Schema({
  id:    { type: Number, required: true },
  front: { type: String, required: true },
  back:  { type: String, required: true },
}, { _id: false });

const flashcardSetSchema = new mongoose.Schema({
  topic:      { type: String, required: true },
  flashcards: [cardSchema],
  numCards:   { type: Number, required: true },
}, { timestamps: true });

module.exports = mongoose.model('FlashcardSet', flashcardSetSchema);
