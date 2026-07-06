import React, { useState, useEffect } from 'react';
import api from '../api.js';
import './FlashcardGenerator.css';

function FlashcardGenerator() {
  const [topic, setTopic] = useState('');
  const [numCards, setNumCards] = useState(10);
  const [cards, setCards] = useState([]);
  const [flipped, setFlipped] = useState({});
  const [currentIndex, setCurrentIndex] = useState(0);
  const [viewMode, setViewMode] = useState('stack');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [savedSets, setSavedSets] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const [savedMsg, setSavedMsg] = useState('');

  useEffect(() => {
    if (showHistory) fetchHistory();
  }, [showHistory]);

  const fetchHistory = async () => {
    try {
      const res = await api.get('/api/flashcards/history');
      setSavedSets(res.data.sets || []);
    } catch {
      setSavedSets([]);
    }
  };

  const loadSet = async (id) => {
    try {
      const res = await api.get(`/api/flashcards/${id}`);
      setCards(res.data.flashcards || []);
      setTopic(res.data.topic);
      setFlipped({});
      setCurrentIndex(0);
      setShowHistory(false);
      setSavedMsg('');
    } catch {
      alert('Failed to load flashcard set.');
    }
  };

  const deleteSet = async (id, e) => {
    e.stopPropagation();
    try {
      await api.delete(`/api/flashcards/${id}`);
      setSavedSets((prev) => prev.filter((s) => s._id !== id));
    } catch {
      alert('Failed to delete set.');
    }
  };

  const generateCards = async () => {
    if (!topic.trim()) return;
    setLoading(true); setError(''); setCards([]); setFlipped({}); setCurrentIndex(0); setSavedMsg('');
    try {
      const res = await api.post('/api/flashcards/generate', { topic, numCards });
      setCards(res.data.flashcards || []);
      if (res.data.setId) setSavedMsg('✅ Saved to MongoDB');
    } catch {
      setError('Failed to generate flashcards. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const toggleFlip = (id) => setFlipped((prev) => ({ ...prev, [id]: !prev[id] }));
  const next = () => setCurrentIndex((i) => Math.min(i + 1, cards.length - 1));
  const prev = () => setCurrentIndex((i) => Math.max(i - 1, 0));
  const currentCard = cards[currentIndex];
  const formatDate = (iso) => new Date(iso).toLocaleDateString();

  return (
    <div className="flashcard-generator">
      <div className="page-header">
        <h1>🃏 Flashcard Maker</h1>
        <p>Generate smart study flashcards for quick revision and memorization</p>
      </div>

      <div className="card fc-form">
        <div className="fc-form-row">
          <div className="input-group">
            <label htmlFor="fc-topic">Topic</label>
            <input id="fc-topic" type="text" value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && generateCards()}
              placeholder="e.g. Human Anatomy, JavaScript ES6, French Revolution..." />
          </div>
          <div className="input-group">
            <label htmlFor="fc-count">Cards</label>
            <select id="fc-count" value={numCards} onChange={(e) => setNumCards(Number(e.target.value))}>
              {[5, 10, 15, 20].map((n) => <option key={n} value={n}>{n}</option>)}
            </select>
          </div>
        </div>
        <div className="form-actions">
          <button className="btn btn-primary" onClick={generateCards} disabled={loading || !topic.trim()}>
            {loading ? <><span className="spinner" /> Generating...</> : '✨ Generate Flashcards'}
          </button>
          <button className="btn btn-outline" onClick={() => setShowHistory(!showHistory)}>
            💾 {showHistory ? 'Hide Saved' : 'Saved Sets'}
          </button>
        </div>
        {savedMsg && <p className="saved-msg">{savedMsg}</p>}
      </div>

      {/* Saved Sets Panel */}
      {showHistory && (
        <div className="card history-panel">
          <h3>💾 Saved Flashcard Sets</h3>
          {savedSets.length === 0
            ? <p className="no-data">No saved sets yet. Generate some flashcards first!</p>
            : <div className="sets-grid">
                {savedSets.map((s) => (
                  <div key={s._id} className="set-card" onClick={() => loadSet(s._id)}>
                    <div className="set-topic">{s.topic}</div>
                    <div className="set-meta">
                      <span>🃏 {s.numCards} cards</span>
                      <span>{formatDate(s.createdAt)}</span>
                    </div>
                    <div className="set-actions">
                      <span className="load-hint">Click to load →</span>
                      <button className="del-btn" onClick={(e) => deleteSet(s._id, e)} title="Delete">🗑</button>
                    </div>
                  </div>
                ))}
              </div>
          }
        </div>
      )}

      {error && <div className="error-msg">{error}</div>}

      {cards.length > 0 && (
        <div className="fc-section">
          <div className="fc-toolbar">
            <span className="fc-count-label">{cards.length} flashcards — <strong>{topic}</strong></span>
            <div className="view-toggle">
              <button className={`toggle-btn ${viewMode === 'stack' ? 'active' : ''}`} onClick={() => setViewMode('stack')}>Stack View</button>
              <button className={`toggle-btn ${viewMode === 'grid'  ? 'active' : ''}`} onClick={() => setViewMode('grid')}>Grid View</button>
            </div>
          </div>

          {viewMode === 'stack' && currentCard && (
            <div className="stack-view">
              <div className="progress-bar">
                <div className="progress-fill" style={{ width: `${((currentIndex + 1) / cards.length) * 100}%` }} />
              </div>
              <p className="card-counter">{currentIndex + 1} / {cards.length}</p>

              <div className={`flashcard ${flipped[currentCard.id] ? 'flipped' : ''}`}
                onClick={() => toggleFlip(currentCard.id)} role="button" tabIndex={0}
                onKeyDown={(e) => e.key === 'Enter' && toggleFlip(currentCard.id)}>
                <div className="flashcard-inner">
                  <div className="flashcard-front">
                    <span className="fc-label">QUESTION</span>
                    <p>{currentCard.front}</p>
                    <span className="flip-hint">Click to flip</span>
                  </div>
                  <div className="flashcard-back">
                    <span className="fc-label">ANSWER</span>
                    <p>{currentCard.back}</p>
                  </div>
                </div>
              </div>

              <div className="stack-nav">
                <button className="btn btn-outline" onClick={prev} disabled={currentIndex === 0}>← Prev</button>
                <button className="btn btn-secondary" onClick={() => toggleFlip(currentCard.id)}>
                  {flipped[currentCard.id] ? '🔄 Show Front' : '🔄 Flip Card'}
                </button>
                <button className="btn btn-outline" onClick={next} disabled={currentIndex === cards.length - 1}>Next →</button>
              </div>
            </div>
          )}

          {viewMode === 'grid' && (
            <div className="fc-grid">
              {cards.map((card) => (
                <div key={card.id} className={`flashcard-mini ${flipped[card.id] ? 'flipped' : ''}`}
                  onClick={() => toggleFlip(card.id)} role="button" tabIndex={0}
                  onKeyDown={(e) => e.key === 'Enter' && toggleFlip(card.id)}>
                  <div className="fc-mini-inner">
                    <div className="fc-mini-front"><span className="fc-label-sm">Q</span><p>{card.front}</p></div>
                    <div className="fc-mini-back"><span className="fc-label-sm">A</span><p>{card.back}</p></div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default FlashcardGenerator;
