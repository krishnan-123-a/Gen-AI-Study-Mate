import React, { useState } from 'react';
import axios from 'axios';
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

  const generateQuiz = async () => {
    if (!topic.trim()) return;
    setLoading(true);
    setError('');
    setQuestions([]);
    setAnswers({});
    setSubmitted(false);

    try {
      const res = await axios.post('/api/quiz/generate', { topic, numQuestions, difficulty });
      setQuestions(res.data.questions || []);
    } catch {
      setError('Failed to generate quiz. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const selectAnswer = (qId, option) => {
    if (submitted) return;
    setAnswers((prev) => ({ ...prev, [qId]: option }));
  };

  const submitQuiz = () => setSubmitted(true);

  const getScore = () =>
    questions.filter((q) => answers[q.id] === q.answer).length;

  const getOptionClass = (q, option) => {
    if (!submitted) {
      return answers[q.id] === option ? 'selected' : '';
    }
    if (option === q.answer) return 'correct';
    if (answers[q.id] === option && option !== q.answer) return 'wrong';
    return '';
  };

  const allAnswered = questions.length > 0 && questions.every((q) => answers[q.id]);

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
            <input
              id="quiz-topic"
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="e.g. World War II, Python basics, Algebra..."
            />
          </div>
          <div className="input-group">
            <label htmlFor="num-questions">Questions</label>
            <select
              id="num-questions"
              value={numQuestions}
              onChange={(e) => setNumQuestions(Number(e.target.value))}
            >
              {[3, 5, 7, 10].map((n) => (
                <option key={n} value={n}>{n}</option>
              ))}
            </select>
          </div>
          <div className="input-group">
            <label htmlFor="difficulty">Difficulty</label>
            <select
              id="difficulty"
              value={difficulty}
              onChange={(e) => setDifficulty(e.target.value)}
            >
              <option value="easy">Easy</option>
              <option value="medium">Medium</option>
              <option value="hard">Hard</option>
            </select>
          </div>
        </div>
        <button className="btn btn-primary" onClick={generateQuiz} disabled={loading || !topic.trim()}>
          {loading ? <><span className="spinner" /> Generating...</> : '🎲 Generate Quiz'}
        </button>
      </div>

      {error && <div className="error-msg">{error}</div>}

      {questions.length > 0 && (
        <div className="quiz-questions">
          {submitted && (
            <div className="score-banner">
              🏆 Score: {getScore()} / {questions.length}
              {getScore() === questions.length && ' — Perfect! 🎉'}
            </div>
          )}

          {questions.map((q, i) => (
            <div key={q.id} className="card question-card">
              <p className="question-text">
                <span className="q-num">Q{i + 1}.</span> {q.question}
              </p>
              <div className="options">
                {q.options.map((opt) => (
                  <button
                    key={opt}
                    className={`option-btn ${getOptionClass(q, opt)}`}
                    onClick={() => selectAnswer(q.id, opt)}
                    disabled={submitted}
                  >
                    {opt}
                  </button>
                ))}
              </div>
              {submitted && answers[q.id] !== q.answer && (
                <p className="correct-answer">✅ Correct: {q.answer}</p>
              )}
              {submitted && q.explanation && (
                <p className="explanation">💡 {q.explanation}</p>
              )}
            </div>
          ))}

          {!submitted && (
            <button
              className="btn btn-primary submit-btn"
              onClick={submitQuiz}
              disabled={!allAnswered}
            >
              Submit Quiz
            </button>
          )}

          {submitted && (
            <button className="btn btn-outline" onClick={generateQuiz}>
              🔄 New Quiz
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export default QuizGenerator;
