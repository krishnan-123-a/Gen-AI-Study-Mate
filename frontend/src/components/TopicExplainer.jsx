import React, { useState } from 'react';
import api from '../api.js';
import './TopicExplainer.css';

function TopicExplainer() {
  const [topic, setTopic] = useState('');
  const [level, setLevel] = useState('beginner');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const explain = async () => {
    if (!topic.trim()) return;
    setLoading(true); setError(''); setResult(null);
    try {
      const res = await api.post('/api/topics/explain', { topic, level });
      setResult(res.data);
    } catch {
      setError('Failed to get explanation. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="topic-explainer">
      <div className="page-header">
        <h1>📚 Topic Explainer</h1>
        <p>Enter any topic and get a structured, AI-generated explanation</p>
      </div>

      <div className="card topic-form">
        <div className="form-row">
          <div className="input-group">
            <label htmlFor="topic-input">Topic</label>
            <input id="topic-input" type="text" value={topic}
              onChange={(e) => setTopic(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && explain()}
              placeholder="e.g. Binary Search, Photosynthesis, Newton's Laws..." />
          </div>
          <div className="input-group level-select">
            <label htmlFor="level-select">Level</label>
            <select id="level-select" value={level} onChange={(e) => setLevel(e.target.value)}>
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
        </div>
        <button className="btn btn-primary" onClick={explain} disabled={loading || !topic.trim()}>
          {loading ? <><span className="spinner" /> Explaining...</> : '📖 Explain Topic'}
        </button>
      </div>

      {error && <div className="error-msg">{error}</div>}

      {result && (
        <div className="topic-result">
          <div className="card result-section"><h2>📝 Explanation</h2><p>{result.explanation}</p></div>

          {result.keyPoints?.length > 0 && (
            <div className="card result-section">
              <h2>🔑 Key Points</h2>
              <ul className="key-points">{result.keyPoints.map((pt, i) => <li key={i}>{pt}</li>)}</ul>
            </div>
          )}

          {result.realWorldExample && (
            <div className="card result-section example-box">
              <h2>💡 Real-World Example</h2><p>{result.realWorldExample}</p>
            </div>
          )}

          <div className="two-col">
            {result.prerequisites?.length > 0 && (
              <div className="card result-section">
                <h2>⬅️ Prerequisites</h2>
                <div className="tag-list">{result.prerequisites.map((p, i) => <span key={i} className="tag tag-prereq">{p}</span>)}</div>
              </div>
            )}
            {result.nextTopics?.length > 0 && (
              <div className="card result-section">
                <h2>➡️ What to Learn Next</h2>
                <div className="tag-list">{result.nextTopics.map((t, i) => <span key={i} className="tag tag-next">{t}</span>)}</div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default TopicExplainer;
