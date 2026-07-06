# 🤖 Gen-AI Study Mate

An intelligent AI-powered study companion that helps students learn smarter. Built with React, Node.js/Express, and OpenAI's GPT models.

## ✨ Features

| Feature | Description |
|---|---|
| 💬 **AI Chat Tutor** | Conversational AI tutor that answers questions and explains concepts |
| 📚 **Topic Explainer** | Structured explanations with key points, prerequisites & next steps |
| 🎯 **Quiz Generator** | Auto-generated multiple-choice quizzes with instant grading |
| 🃏 **Flashcard Maker** | Smart study flashcards with flip animation (stack & grid views) |

## 🗂️ Project Structure

```
Gen-AI-Study-Mate/
├── backend/
│   ├── config/
│   │   └── openai.js          # OpenAI client setup
│   ├── routes/
│   │   ├── chat.js            # AI chat endpoint
│   │   ├── topics.js          # Topic explain & summary endpoints
│   │   ├── quiz.js            # Quiz generation endpoint
│   │   └── flashcards.js      # Flashcard generation endpoint
│   └── server.js              # Express server entry point
├── frontend/
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── components/
│       │   ├── Navbar.js/css
│       │   ├── Home.js/css
│       │   ├── ChatBot.js/css
│       │   ├── TopicExplainer.js/css
│       │   ├── QuizGenerator.js/css
│       │   └── FlashcardGenerator.js/css
│       ├── App.js
│       ├── App.css
│       ├── index.js
│       └── index.css
├── .env.example
├── .gitignore
├── package.json
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) v16+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/krishnan-123-a/Gen-AI-Study-Mate.git
   cd Gen-AI-Study-Mate
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

3. **Install backend dependencies**
   ```bash
   npm install
   ```

4. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### Running the App

**Start the backend server:**
```bash
npm run dev
```
Backend runs at `http://localhost:5000`

**Start the React frontend (in a new terminal):**
```bash
cd frontend
npm start
```
Frontend runs at `http://localhost:3000`

## 🔧 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Health check |
| POST | `/api/chat` | AI chat message |
| POST | `/api/topics/explain` | Explain a topic |
| POST | `/api/topics/summary` | Summarize text |
| POST | `/api/quiz/generate` | Generate a quiz |
| POST | `/api/flashcards/generate` | Generate flashcards |

## 🛠️ Tech Stack

- **Frontend:** React 18, CSS3 (no framework)
- **Backend:** Node.js, Express
- **AI:** OpenAI GPT-4o-mini (configurable)
- **HTTP Client:** Axios

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
