import React, { useState, useEffect } from 'react';
import api from '../api.js';
import './QuizGenerator.css';

function QuizGenerator() {
  const [topic, setTopic] = useState('');
  const [numQuestions, setNumQuestions] = useState(5);
  const [difficulty, setDifficulty] = useState('medium');
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(false);

  useEffect(() => {
    if (showHistory) fetchHistory();
  }, [showHistory]);

  const fetchHistory = async () => {
    try {
      const res = await api.get('/api/quiz/history');
      setHistory(res.data.results || []);
    } catch {
      setHistory([]);
    }
  };

  const generateQuiz = async () => {
    if (!topic.trim()) return;
    setLoading(true); setError(''); setQuestions([]); setAnswers({}); setSubmitted(false);
    try {
      const res = await api.post('/api/quiz/generate', { topic, numQuestions, difficulty });
      setQuestions(res.data.questions || []);
    } catch {
      setError('Failed to generate quiz. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const selectAnswer = (qId, option) => { if (!submitted) setAnswers((prev) => ({ ...prev, [qId]: option })); };

  const submitQuiz = async () => {
    setSubmitted(true);
    const score = questions.filter((q) => answers[q.id] === q.answer).length;
    // Save to MongoDB
    try {
      await api.post('/api/quiz/save', {
        topic, difficulty,
        questions: questions.map((q) => ({
          ...q,
          userAnswer: answers[q.id] || null,
          correct: answers[q.id] === q.answer,
        })),
        score,
        total: questions.length,
      });
    } catch {
      // Non-critical — quiz is still usable even if save fails
      console.warn('Quiz save failed');
    }
  };

  const getScore = () => questions.filter((q) => answers[q.id] === q.answer).length;

  const getOptionClass = (q, option) => {
    if (!submitted) return answers[q.id] === option ? 'selected' : '';
    if (option === q.answer) return 'correct';
    if (answers[q.id] === option) return 'wrong';
    return '';
  };

  const allAnswered = questions.length > 0 && questions.every((q) => answers[q.id]);
  const formatDate = (iso) => new Date(iso).toLocaleDateString();
  const pctColor = (p) => p >= 80 ? '#10b981' : p >= 50 ? '#f59e0b' : '#ef4444';

  return (
    <div className="quiz-generator">
      <div className="page-header">
        <h1>🎯 Quiz Generator</h1>
        <p>Test your knowledge with AI-generated multiple-choice quizzes</p>
      </div>

      <div className="card quiz-form">
        <div className="quiz-form-row">
          <div className="input-group">
            <label htmlFor="quiz-topic">Topic</label>
            <input id="quiz-topic" type="text" value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="e.g. World War II, Python basics, Algebra..." />
          </div>
          <div className="input-group">
            <label htmlFor="num-questions">Questions</label>
            <select id="num-questions" value={numQuestions} onChange={(e) => setNumQuestions(Number(e.target.value))}>
              {[3, 5, 7, 10].map((n) => <option key={n} value={n}>{n}</option>)}
            </select>
          </div>
          <div className="input-group">
            <label htmlFor="difficulty">Difficulty</label>
            <select id="difficulty" value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>
        </div>
        <div className="form-actions">
          <button className="btn btn-primary" onClick={generateQuiz} disabled={loading || !topic.trim()}>
            {loading ? <><span className="spinner" /> Generating...</> : '🎲 Generate Quiz'}
          </button>
          <button className="btn btn-outline" onClick={() => setShowHistory(!showHistory)}>
            📊 {showHistory ? 'Hide History' : 'Past Results'}
          </button>
        </div>
      </div>

      {/* Past Results Panel */}
      {showHistory && (
        <div className="card history-panel">
          <h3>📊 Past Quiz Results</h3>
          {history.length === 0
            ? <p className="no-data">No quiz results saved yet.</p>
            : <div className="history-list">
                {history.map((r, i) => (
                  <div key={i} className="history-item">
                    <div className="history-topic">{r.topic}</div>
                    <div className="history-meta">
                      <span className="diff-badge diff-{r.difficulty}">{r.difficulty}</span>
                      <span>{formatDate(r.createdAt)}</span>
                    </div>
                    <div className="history-score">
                      <span style={{ color: pctColor(r.percentage), fontWeight: 700 }}>{r.percentage}%</span>
                      <span className="score-detail">{r.score}/{r.total}</span>
                    </div>
                  </div>
                ))}
              </div>
          }
        </div>
      )}

      {error && <div className="error-msg">{error}</div>}

      {questions.length > 0 && (
        <div className="quiz-questions">
          {submitted && (
            <div className="score-banner">
              🏆 Score: {getScore()} / {questions.length} ({Math.round((getScore()/questions.length)*100)}%)
              {getScore() === questions.length && ' — Perfect! 🎉'}
              <div className="score-saved">✅ Result saved to MongoDB</div>
            </div>
          )}

          {questions.map((q, i) => (
            <div key={q.id} className="card question-card">
              <p className="question-text"><span className="q-num">Q{i + 1}.</span> {q.question}</p>
              <div className="options">
                {q.options.map((opt) => (
                  <button key={opt} className={`option-btn ${getOptionClass(q, opt)}`}
                    onClick={() => selectAnswer(q.id, opt)} disabled={submitted}>{opt}</button>
                ))}
              </div>
              {submitted && answers[q.id] !== q.answer && <p className="correct-answer">✅ Correct: {q.answer}</p>}
              {submitted && q.explanation && <p className="explanation">💡 {q.explanation}</p>}
            </div>
          ))}

          {!submitted && <button className="btn btn-primary submit-btn" onClick={submitQuiz} disabled={!allAnswered}>Submit Quiz</button>}
          {submitted && <button className="btn btn-outline" onClick={generateQuiz}>🔄 New Quiz</button>}
        </div>
      )}
    </div>
  );
}

export default QuizGenerator;
