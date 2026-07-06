import React, { useState, useEffect } from 'react';
import './App.css';
import Navbar from './components/Navbar.jsx';
import ChatBot from './components/ChatBot.jsx';
import TopicExplainer from './components/TopicExplainer.jsx';
import QuizGenerator from './components/QuizGenerator.jsx';
import FlashcardGenerator from './components/FlashcardGenerator.jsx';
import Home from './components/Home.jsx';
import api from './api.js';

const PAGES = {
  HOME: 'home',
  CHAT: 'chat',
  TOPICS: 'topics',
  QUIZ: 'quiz',
  FLASHCARDS: 'flashcards',
};

function App() {
  const [currentPage, setCurrentPage] = useState(PAGES.HOME);
  const [demoMode, setDemoMode] = useState(false);

  useEffect(() => {
    api.get('/api/status')
      .then((res) => setDemoMode(res.data.demoMode))
      .catch(() => {});
  }, []);

  const renderPage = () => {
    switch (currentPage) {
      case PAGES.CHAT:        return <ChatBot />;
      case PAGES.TOPICS:      return <TopicExplainer />;
      case PAGES.QUIZ:        return <QuizGenerator />;
      case PAGES.FLASHCARDS:  return <FlashcardGenerator />;
      default:                return <Home onNavigate={setCurrentPage} />;
    }
  };

  return (
    <div className="app">
      <Navbar currentPage={currentPage} onNavigate={setCurrentPage} pages={PAGES} />

      {demoMode && (
        <div className="demo-banner" role="status">
          🧪 <strong>Demo Mode</strong> — All features work with sample data.
          Add your <code>OPENAI_API_KEY</code> in <code>.env</code> for live AI responses.
        </div>
      )}

      <main className="main-content">
        {renderPage()}
      </main>
    </div>
  );
}

export default App;
