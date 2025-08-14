@echo off
echo ==========================================
echo    StudyMate - AI Educational Platform
echo    COMPLETE VERSION WITH GMAIL LOGIN
echo ==========================================
echo.
echo ✅ Features Available:
echo    📧 Gmail Login (any Gmail + any password)
echo    📝 Quiz Page (10 sample questions)
echo    📁 Study Materials (PDF upload + AI Q&A)
echo    🎯 Quiz Mode (AI-generated quizzes)
echo    📊 Dashboard (learning analytics)
echo.
echo 🚀 Starting StudyMate application...
echo.
echo 🌐 Opening in your default browser...
echo 🔗 URL: http://localhost:8535
echo.
echo 💡 Login with any Gmail address + any password
echo 📝 Try the new Quiz Page with 10 questions!
echo.
echo ⚠️ Press Ctrl+C to stop the application
echo ==========================================
echo.

python -m streamlit run app_clear_text.py --server.port 8535

echo.
echo 👋 StudyMate session ended. Thank you!
pause
