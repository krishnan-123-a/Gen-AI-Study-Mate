import React, { useState } from 'react';
import './Navbar.css';

function Navbar({ currentPage, onNavigate, pages }) {
  const [menuOpen, setMenuOpen] = useState(false);

  const navItems = [
    { id: pages.HOME, label: 'Home', icon: '🏠' },
    { id: pages.CHAT, label: 'AI Chat', icon: '💬' },
    { id: pages.TOPICS, label: 'Topics', icon: '📚' },
    { id: pages.QUIZ, label: 'Quiz', icon: '🎯' },
    { id: pages.FLASHCARDS, label: 'Flashcards', icon: '🃏' },
  ];

  const handleNav = (id) => {
    onNavigate(id);
    setMenuOpen(false);
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand" onClick={() => handleNav(pages.HOME)}>
        <span className="brand-icon">🤖</span>
        <span className="brand-name">Gen-AI Study Mate</span>
      </div>

      <button
        className="hamburger"
        onClick={() => setMenuOpen(!menuOpen)}
        aria-label="Toggle menu"
        aria-expanded={menuOpen}
      >
        {menuOpen ? '✕' : '☰'}
      </button>

      <ul className={`nav-links ${menuOpen ? 'open' : ''}`}>
        {navItems.map((item) => (
          <li key={item.id}>
            <button
              className={`nav-link ${currentPage === item.id ? 'active' : ''}`}
              onClick={() => handleNav(item.id)}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Navbar;
