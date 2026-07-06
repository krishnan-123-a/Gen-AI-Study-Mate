import React, { useState } from 'react';
import './App.css';
import Navbar from './components/Navbar.jsx';
import ChatBot from './components/ChatBot.jsx';
import TopicExplainer from './components/TopicExplainer.jsx';
import QuizGenerator from './components/QuizGenerator.jsx';
import FlashcardGenerator from './components/FlashcardGenerator.jsx';
import Home from './components/Home.jsx';

const PAGES = {
  HOME: 'home',
  CHAT: 'chat',
  TOPICS: 'topics',
  QUIZ: 'quiz',
  FLASHCARDS: 'flashcards',
};

function App() {
  const [currentPage, setCurrentPage] = useState(PAGES.HOME);

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
      <main className="main-content">
        {renderPage()}
      </main>
    </div>
  );
}

export default App;
