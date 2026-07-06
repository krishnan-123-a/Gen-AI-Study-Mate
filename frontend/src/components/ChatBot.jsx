import React, { useState, useRef, useEffect } from 'react';
import api from '../api.js';
import './ChatBot.css';

function ChatBot() {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: "Hi! I'm your Gen-AI Study Mate 👋 Ask me anything — a concept, a topic, a problem. I'm here to help you learn!" },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [sessions, setSessions] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

  // Load chat history list when history panel is opened
  useEffect(() => {
    if (showHistory) fetchHistory();
  }, [showHistory]);

  const fetchHistory = async () => {
    try {
      const res = await api.get('/api/chat/history');
      setSessions(res.data.sessions || []);
    } catch {
      setSessions([]);
    }
  };

  const loadSession = async (sid) => {
    try {
      const res = await api.get(`/api/chat/session/${sid}`);
      setMessages(res.data.messages);
      setSessionId(sid);
      setShowHistory(false);
    } catch {
      alert('Failed to load session.');
    }
  };

  const deleteSession = async (sid, e) => {
    e.stopPropagation();
    try {
      await api.delete(`/api/chat/session/${sid}`);
      setSessions((prev) => prev.filter((s) => s.sessionId !== sid));
    } catch {
      alert('Failed to delete session.');
    }
  };

  const sendMessage = async () => {
    const text = input.trim();
    if (!text || loading) return;

    const userMsg = { role: 'user', content: text };
    const updatedMessages = [...messages, userMsg];
    setMessages(updatedMessages);
    setInput('');
    setLoading(true);

    try {
      const history = updatedMessages
        .filter((m) => m.role !== 'system')
        .slice(1)
        .map(({ role, content }) => ({ role, content }));

      const res = await api.post('/api/chat', { message: text, history, sessionId });
      setMessages((prev) => [...prev, { role: 'assistant', content: res.data.reply }]);
      if (res.data.sessionId) setSessionId(res.data.sessionId);
    } catch {
      setMessages((prev) => [...prev, { role: 'assistant', content: '⚠️ Sorry, I ran into an issue. Please try again.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } };

  const newChat = () => {
    setMessages([{ role: 'assistant', content: "New chat started! What would you like to learn about?" }]);
    setSessionId(null);
  };

  const formatDate = (iso) => new Date(iso).toLocaleString(undefined, { dateStyle: 'short', timeStyle: 'short' });
  const previewMsg = (session) => {
    const userMsgs = session.messages.filter((m) => m.role === 'user');
    return userMsgs.length > 0 ? userMsgs[0].content.slice(0, 50) + '...' : 'Empty session';
  };

  return (
    <div className="chatbot">
      <div className="page-header">
        <h1>💬 AI Chat Tutor</h1>
        <p>Ask any question and get clear explanations from your AI tutor</p>
      </div>

      <div className="chat-layout">
        {/* History Sidebar */}
        <div className={`chat-sidebar ${showHistory ? 'open' : ''}`}>
          <div className="sidebar-header">
            <span>💾 Saved Sessions</span>
            <button className="close-btn" onClick={() => setShowHistory(false)}>✕</button>
          </div>
          <div className="session-list">
            {sessions.length === 0 && <p className="no-sessions">No saved sessions yet.</p>}
            {sessions.map((s) => (
              <div key={s.sessionId} className="session-item" onClick={() => loadSession(s.sessionId)}>
                <div className="session-preview">{previewMsg(s)}</div>
                <div className="session-meta">
                  <span>{formatDate(s.updatedAt)}</span>
                  <button className="del-btn" onClick={(e) => deleteSession(s.sessionId, e)} title="Delete">🗑</button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Chat Window */}
        <div className="chat-container card">
          <div className="chat-header">
            <div className="chat-status">
              <span className="status-dot"></span>
              <span>AI Tutor Online</span>
              {sessionId && <span className="session-badge">Session saved ✓</span>}
            </div>
            <div className="chat-header-actions">
              <button className="btn btn-outline btn-sm" onClick={() => setShowHistory(true)}>📂 History</button>
              <button className="btn btn-outline btn-sm" onClick={newChat}>+ New Chat</button>
            </div>
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
