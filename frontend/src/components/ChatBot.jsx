import React, { useState, useRef, useEffect } from 'react';
import api from '../api.js';
import './ChatBot.css';

function ChatBot() {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: "Hi! I'm your Gen-AI Study Mate 👋 Ask me anything — a concept, a topic, a problem. I'm here to help you learn!" },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

  const sendMessage = async () => {
    const text = input.trim();
    if (!text || loading) return;

    const userMsg = { role: 'user', content: text };
    const updatedMessages = [...messages, userMsg];
    setMessages(updatedMessages);
    setInput('');
    setLoading(true);

    try {
      const history = updatedMessages.slice(1).map(({ role, content }) => ({ role, content }));
      const res = await api.post('/api/chat', { message: text, history });
      setMessages((prev) => [...prev, { role: 'assistant', content: res.data.reply }]);
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: '⚠️ Sorry, I ran into an issue. Please try again.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } };

  const clearChat = () => setMessages([{ role: 'assistant', content: "Chat cleared! What would you like to learn about?" }]);

  return (
    <div className="chatbot">
      <div className="page-header">
        <h1>💬 AI Chat Tutor</h1>
        <p>Ask any question and get clear explanations from your AI tutor</p>
      </div>

      <div className="chat-container card">
        <div className="chat-header">
          <div className="chat-status"><span className="status-dot"></span><span>AI Tutor Online</span></div>
          <button className="btn btn-outline btn-sm" onClick={clearChat}>Clear Chat</button>
        </div>

        <div className="messages" role="log" aria-live="polite">
          {messages.map((msg, i) => (
            <div key={i} className={`message ${msg.role}`}>
              <div className="message-avatar">{msg.role === 'assistant' ? '🤖' : '👤'}</div>
              <div className="message-bubble"><pre className="message-text">{msg.content}</pre></div>
            </div>
          ))}
          {loading && (
            <div className="message assistant">
              <div className="message-avatar">🤖</div>
              <div className="message-bubble typing"><span></span><span></span><span></span></div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chat-input-area">
          <textarea className="chat-input" value={input} onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown} placeholder="Ask a question... (Enter to send, Shift+Enter for new line)"
            rows={2} disabled={loading} aria-label="Chat message input" />
          <button className="btn btn-primary send-btn" onClick={sendMessage}
            disabled={loading || !input.trim()} aria-label="Send message">
            {loading ? <span className="spinner" /> : '➤'}
          </button>
        </div>
      </div>

      <div className="chat-suggestions">
        <p className="suggestions-label">Try asking:</p>
        <div className="suggestion-chips">
          {['Explain recursion in simple terms', 'What is machine learning?', 'How does photosynthesis work?', 'Explain the Pythagorean theorem'].map((s) => (
            <button key={s} className="chip" onClick={() => setInput(s)} disabled={loading}>{s}</button>
          ))}
        </div>
      </div>
    </div>
  );
}

export default ChatBot;
