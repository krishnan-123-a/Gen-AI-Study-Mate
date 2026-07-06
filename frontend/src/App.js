import React, { useState } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import ChatBot from './components/ChatBot';
import TopicExplainer from './components/TopicExplainer';
import QuizGenerator from './components/QuizGenerator';
import FlashcardGenerator from './components/FlashcardGenerator';
import Home from './components/Home';

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
      case PAGES.CHAT:
        return <ChatBot />;
      case PAGES.TOPICS:
        return <TopicExplainer />;
      case PAGES.QUIZ:
        return <QuizGenerator />;
      case PAGES.FLASHCARDS:
        return <FlashcardGenerator />;
      default:
        return <Home onNavigate={setCurrentPage} />;
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
