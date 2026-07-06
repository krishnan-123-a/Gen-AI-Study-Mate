import React from 'react';
import './Home.css';

function Home({ onNavigate }) {
  const features = [
    { icon: '💬', title: 'AI Chat Tutor',    description: 'Ask anything and get clear, intelligent explanations from your personal AI tutor.', page: 'chat',       color: '#4f46e5' },
    { icon: '📚', title: 'Topic Explainer',  description: 'Deep-dive into any topic with structured explanations, key points, and prerequisites.', page: 'topics',  color: '#06b6d4' },
    { icon: '🎯', title: 'Quiz Generator',   description: 'Test your knowledge with AI-generated multiple-choice quizzes on any subject.',       page: 'quiz',       color: '#f59e0b' },
    { icon: '🃏', title: 'Flashcard Maker',  description: 'Create smart study flashcards instantly for quick revision and memorization.',         page: 'flashcards', color: '#10b981' },
  ];

  return (
    <div className="home">
      <div className="hero">
        <div className="hero-badge">✨ Powered by Generative AI</div>
        <h1 className="hero-title">
          Learn Smarter with <span>Gen-AI Study Mate</span>
        </h1>
        <p className="hero-subtitle">
          Your intelligent AI-powered study companion that explains topics, generates quizzes,
          creates flashcards, and answers all your questions — 24/7.
        </p>
        <div className="hero-actions">
          <button className="btn btn-primary" onClick={() => onNavigate('chat')}>💬 Start Chatting</button>
          <button className="btn btn-outline" onClick={() => onNavigate('topics')}>📚 Explore Topics</button>
        </div>
      </div>

      <div className="features-grid">
        {features.map((f) => (
          <div key={f.page} className="feature-card"
            onClick={() => onNavigate(f.page)} role="button" tabIndex={0}
            onKeyDown={(e) => e.key === 'Enter' && onNavigate(f.page)}
            aria-label={`Go to ${f.title}`}>
            <div className="feature-icon" style={{ background: `${f.color}15`, color: f.color }}>{f.icon}</div>
            <h3>{f.title}</h3>
            <p>{f.description}</p>
            <span className="feature-arrow">→</span>
          </div>
        ))}
      </div>

      <div className="stats-bar">
        <div className="stat"><span className="stat-num">∞</span><span className="stat-label">Topics Available</span></div>
        <div className="stat"><span className="stat-num">4</span><span className="stat-label">Learning Tools</span></div>
        <div className="stat"><span className="stat-num">24/7</span><span className="stat-label">AI Availability</span></div>
      </div>
    </div>
  );
}

export default Home;
