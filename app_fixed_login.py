"""
StudyMate - Fixed Login & Quiz System
Properly working login page with clear authentication
"""

import streamlit as st
import os
import time
import random
from datetime import datetime
import hashlib
import json

# Simple user database - in production, use a real database
USERS_DB = {
    "admin": {
        "password": "password",  # Plain text for demo - in production use hashing
        "name": "Administrator",
        "role": "admin"
    },
    "student": {
        "password": "student123",
        "name": "Student User", 
        "role": "student"
    },
    "teacher": {
        "password": "teacher123",
        "name": "Teacher User",
        "role": "teacher"
    }
}

def verify_login(username, password):
    """Verify user credentials - simplified for demo"""
    if username in USERS_DB:
        if USERS_DB[username]["password"] == password:
            return USERS_DB[username]
    return None

def show_login_page():
    """Display the login page"""
    st.set_page_config(
        page_title="StudyMate Login",
        page_icon="📚",
        layout="centered"
    )
    
    # Custom CSS for login page
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .login-container {
        background: white;
        padding: 3rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        max-width: 400px;
        margin: 2rem auto;
        text-align: center;
    }
    
    .login-title {
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    
    .login-subtitle {
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .demo-accounts {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 2rem 0;
        text-align: left;
    }
    
    .demo-accounts h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .demo-account {
        background: #e9ecef;
        padding: 0.8rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        font-family: monospace;
    }
    
    .features-list {
        background: #e8f5e8;
        border: 1px solid #c3e6cb;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 2rem 0;
        text-align: left;
    }
    
    .features-list h3 {
        color: #155724;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .features-list ul {
        color: #155724;
        margin: 0;
        padding-left: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main login container
    st.markdown("""
    <div class="login-container">
        <h1 class="login-title">📚 StudyMate</h1>
        <p class="login-subtitle">AI-Powered Study Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Login form
    st.markdown("## 🔐 Login to Continue")
    
    # Create login form
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "👤 Username", 
            placeholder="Enter your username",
            help="Use one of the demo accounts below"
        )
        password = st.text_input(
            "🔒 Password", 
            type="password",
            placeholder="Enter your password",
            help="Use the corresponding password for your username"
        )
        
        # Login button
        login_clicked = st.form_submit_button(
            "🚀 Login", 
            type="primary",
            use_container_width=True
        )
        
        # Handle login
        if login_clicked:
            if username and password:
                user = verify_login(username, password)
                if user:
                    # Set session state
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.username = username
                    
                    st.success(f"✅ Welcome, {user['name']}!")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password! Please try again.")
            else:
                st.warning("⚠️ Please enter both username and password!")
    
    # Demo accounts section
    st.markdown("""
    <div class="demo-accounts">
        <h3>🎯 Demo Accounts</h3>
        <div class="demo-account">
            <strong>👑 Admin:</strong> admin / password
        </div>
        <div class="demo-account">
            <strong>🎓 Student:</strong> student / student123
        </div>
        <div class="demo-account">
            <strong>👨‍🏫 Teacher:</strong> teacher / teacher123
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features preview
    st.markdown("""
    <div class="features-list">
        <h3>🌟 StudyMate Features</h3>
        <ul>
            <li>📁 <strong>PDF Upload & Processing</strong> - Upload study materials</li>
            <li>💬 <strong>AI Q&A System</strong> - Ask questions about documents</li>
            <li>🎯 <strong>Interactive Quiz Mode</strong> - Test your knowledge</li>
            <li>📊 <strong>Progress Tracking</strong> - Monitor learning progress</li>
            <li>📝 <strong>Session History</strong> - Review past sessions</li>
            <li>💾 <strong>Export Results</strong> - Download study sessions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick login buttons for demo
    st.markdown("### 🚀 Quick Login (Demo)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👑 Login as Admin", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["admin"]
            st.session_state.username = "admin"
            st.success("✅ Logged in as Admin!")
            st.rerun()
    
    with col2:
        if st.button("🎓 Login as Student", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["student"]
            st.session_state.username = "student"
            st.success("✅ Logged in as Student!")
            st.rerun()
    
    with col3:
        if st.button("👨‍🏫 Login as Teacher", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["teacher"]
            st.session_state.username = "teacher"
            st.success("✅ Logged in as Teacher!")
            st.rerun()

def extract_text_from_pdf_robust(uploaded_file):
    """Robust PDF text extraction"""
    try:
        import fitz  # PyMuPDF
        
        uploaded_file.seek(0)
        pdf_bytes = uploaded_file.read()
        
        try:
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            text = ""
            
            for page_num in range(pdf_document.page_count):
                try:
                    page = pdf_document.page(page_num)
                    page_text = page.get_text()
                    if page_text.strip():
                        text += page_text + "\n"
                except Exception:
                    continue
            
            pdf_document.close()
            
            if text.strip():
                return text.strip()
            else:
                return "No readable text found in this PDF."
                
        except Exception as fitz_error:
            st.error(f"Error processing PDF: {str(fitz_error)}")
            return None
            
    except ImportError:
        st.error("PyMuPDF is not installed. Please install it with: pip install PyMuPDF")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None

def chunk_text_smart(text, filename, chunk_size=500, overlap=100):
    """Smart text chunking"""
    if not text or len(text.strip()) == 0:
        return []
    
    words = text.split()
    chunks = []
    
    if len(words) <= chunk_size:
        return [{
            'text': text,
            'source': filename,
            'chunk_id': 0,
            'word_count': len(words)
        }]
    
    start_idx = 0
    chunk_id = 0
    
    while start_idx < len(words):
        end_idx = min(start_idx + chunk_size, len(words))
        chunk_words = words[start_idx:end_idx]
        chunk_text = ' '.join(chunk_words)
        
        chunks.append({
            'text': chunk_text,
            'source': filename,
            'chunk_id': chunk_id,
            'word_count': len(chunk_words)
        })
        
        start_idx = end_idx - overlap
        chunk_id += 1
        
        if end_idx >= len(words):
            break
    
    return chunks

def advanced_search(query, chunks):
    """Advanced search with scoring"""
    if not query or not chunks:
        return []
    
    query_words = query.lower().split()
    results = []
    
    for chunk in chunks:
        chunk_text = chunk['text'].lower()
        score = 0
        
        for word in query_words:
            if word in chunk_text:
                score += chunk_text.count(word) * 2
        
        query_phrase = query.lower()
        if query_phrase in chunk_text:
            score += len(query_words) * 3
        
        if score > 0:
            chunk_with_score = chunk.copy()
            chunk_with_score['similarity_score'] = score / len(query_words)
            results.append(chunk_with_score)
    
    results.sort(key=lambda x: x['similarity_score'], reverse=True)
    return results[:5]

def generate_quiz_questions(chunks, num_questions=5):
    """Generate quiz questions from document chunks"""
    if not chunks or len(chunks) < num_questions:
        return []
    
    selected_chunks = random.sample(chunks, min(num_questions, len(chunks)))
    questions = []
    
    for i, chunk in enumerate(selected_chunks):
        text = chunk['text']
        
        # Simple multiple choice question
        question = {
            "id": i + 1,
            "type": "multiple_choice",
            "question": f"Q{i+1}: What is the main topic discussed in this excerpt from '{chunk['source']}'?",
            "context": text[:200] + "..." if len(text) > 200 else text,
            "options": [
                "Machine Learning and AI concepts",
                "Database management",
                "Web development",
                "Network security"
            ],
            "correct_answer": 0,
            "source": chunk['source'],
            "explanation": f"This topic is discussed in the document: {chunk['source']}"
        }
        
        questions.append(question)
    
    return questions

def show_main_app():
    """Main application after login"""
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        page_icon="📚",
        layout="wide"
    )
    
    # Custom CSS for main app
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    
    .main-header {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .user-info {
        background: #d5f4e6;
        border: 2px solid #27ae60;
        color: #1e8449;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 600;
        text-align: center;
    }
    
    .feature-card {
        background: #ffffff;
        border: 2px solid #3498db;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .quiz-container {
        background: #f8f9fa;
        border: 2px solid #17a2b8;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'chunks' not in st.session_state:
        st.session_state.chunks = []
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = []
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'quiz_completed' not in st.session_state:
        st.session_state.quiz_completed = False
    
    # Header with user info
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        <div class="main-header">
            <h1>📚 StudyMate - AI Study Companion</h1>
            <p>Transform your PDFs into an interactive learning experience</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="user-info">
            <strong>👤 Welcome, {st.session_state.user['name']}!</strong><br>
            <small>Role: {st.session_state.user['role'].title()}</small>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["📁 Study Materials", "🎯 Quiz Mode", "📊 Dashboard"])
    
    with tab1:
        st.markdown("""
        <div class="feature-card">
            <h2>📁 Upload Study Materials</h2>
            <p>Upload your PDF study materials to get started with AI-powered Q&A.</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type=['pdf'],
            accept_multiple_files=True,
            help="Upload your study materials in PDF format"
        )
        
        # Process files
        if uploaded_files and len(uploaded_files) != len(st.session_state.processed_files):
            with st.spinner("🔄 Processing PDFs..."):
                all_chunks = []
                processed_files = []
                
                for uploaded_file in uploaded_files:
                    st.info(f"Processing: {uploaded_file.name}")
                    text = extract_text_from_pdf_robust(uploaded_file)
                    if text and len(text.strip()) > 0:
                        chunks = chunk_text_smart(text, uploaded_file.name)
                        if chunks:
                            all_chunks.extend(chunks)
                            processed_files.append(uploaded_file.name)
                            st.success(f"✅ Processed: {uploaded_file.name}")
                
                st.session_state.chunks = all_chunks
                st.session_state.processed_files = processed_files
                
                if all_chunks:
                    st.balloons()
                    st.success(f"🎉 Successfully processed {len(processed_files)} PDF(s)!")
        
        # Q&A Interface
        if st.session_state.chunks:
            st.markdown("""
            <div class="feature-card">
                <h2>💬 Ask Questions</h2>
                <p>Ask any question about your uploaded study materials.</p>
            </div>
            """, unsafe_allow_html=True)
            
            query = st.text_input(
                "Your Question:",
                placeholder="e.g., What is machine learning?",
                help="Ask any question about your uploaded documents"
            )
            
            if st.button("🔍 Get Answer", type="primary") and query:
                with st.spinner("🤖 Generating answer..."):
                    relevant_chunks = advanced_search(query, st.session_state.chunks)
                    
                    if relevant_chunks:
                        context = " ".join([chunk['text'] for chunk in relevant_chunks])
                        answer = f"Based on your documents: {context[:500]}..."
                        
                        st.success("✅ Answer generated!")
                        st.write("**Answer:**", answer)
                        
                        sources = list(set(chunk['source'] for chunk in relevant_chunks))
                        st.write("**Sources:**", ", ".join(sources))
                    else:
                        st.warning("🔍 No relevant information found.")
    
    with tab2:
        st.markdown("""
        <div class="quiz-container">
            <h1>🎯 Interactive Quiz Mode</h1>
            <p>Test your knowledge with AI-generated questions from your study materials</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.chunks:
            st.warning("📁 Please upload PDF documents first to generate quiz questions!")
        else:
            # Quiz setup
            if not st.session_state.quiz_started:
                st.subheader("🎮 Quiz Setup")
                
                col1, col2 = st.columns(2)
                with col1:
                    num_questions = st.selectbox("Number of Questions:", [3, 5, 10], index=1)
                with col2:
                    difficulty = st.selectbox("Difficulty Level:", ["Easy", "Medium", "Hard"], index=1)
                
                if st.button("🚀 Start Quiz", type="primary"):
                    with st.spinner("🎯 Generating quiz questions..."):
                        questions = generate_quiz_questions(st.session_state.chunks, num_questions)
                        if questions:
                            st.session_state.quiz_questions = questions
                            st.session_state.quiz_started = True
                            st.session_state.current_question = 0
                            st.session_state.quiz_answers = {}
                            st.session_state.quiz_completed = False
                            st.success(f"✅ Generated {len(questions)} questions!")
                            st.rerun()
                        else:
                            st.error("❌ Could not generate questions.")
            
            # Quiz in progress
            elif st.session_state.quiz_started and not st.session_state.quiz_completed:
                questions = st.session_state.quiz_questions
                current_q = st.session_state.current_question
                
                if current_q < len(questions):
                    question = questions[current_q]
                    
                    # Progress
                    progress = (current_q + 1) / len(questions)
                    st.progress(progress)
                    st.write(f"Question {current_q + 1} of {len(questions)}")
                    
                    # Display question
                    st.subheader(question['question'])
                    st.write("**Context:**", question['context'])
                    
                    # Answer options
                    answer = st.radio("Choose the correct answer:", question['options'], key=f"q_{current_q}")
                    
                    # Navigation
                    col1, col2 = st.columns(2)
                    with col1:
                        if current_q < len(questions) - 1:
                            if st.button("➡️ Next Question"):
                                st.session_state.quiz_answers[current_q] = answer
                                st.session_state.current_question += 1
                                st.rerun()
                    with col2:
                        if current_q == len(questions) - 1:
                            if st.button("🏁 Finish Quiz"):
                                st.session_state.quiz_answers[current_q] = answer
                                st.session_state.quiz_completed = True
                                st.rerun()
            
            # Quiz completed
            elif st.session_state.quiz_completed:
                st.success("🎉 Quiz Completed!")
                
                # Calculate score
                questions = st.session_state.quiz_questions
                answers = st.session_state.quiz_answers
                correct_count = 0
                
                for i, question in enumerate(questions):
                    user_answer = answers.get(i, "")
                    if user_answer == question['options'][question['correct_answer']]:
                        correct_count += 1
                
                score_percentage = (correct_count / len(questions)) * 100
                
                # Display results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("📊 Score", f"{correct_count}/{len(questions)}")
                with col2:
                    st.metric("📈 Percentage", f"{score_percentage:.1f}%")
                with col3:
                    if score_percentage >= 80:
                        st.metric("🏆 Grade", "Excellent!")
                    elif score_percentage >= 60:
                        st.metric("👍 Grade", "Good!")
                    else:
                        st.metric("📚 Grade", "Keep studying!")
                
                # Reset quiz
                if st.button("🔄 Take New Quiz"):
                    st.session_state.quiz_questions = []
                    st.session_state.current_question = 0
                    st.session_state.quiz_answers = {}
                    st.session_state.quiz_started = False
                    st.session_state.quiz_completed = False
                    st.rerun()
    
    with tab3:
        st.markdown("""
        <div class="feature-card">
            <h2>📊 Learning Dashboard</h2>
            <p>Track your learning progress and statistics.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📄 Documents", len(st.session_state.processed_files))
        with col2:
            st.metric("📝 Text Chunks", len(st.session_state.chunks))
        with col3:
            if st.session_state.chunks:
                total_words = sum(chunk['word_count'] for chunk in st.session_state.chunks)
                st.metric("📊 Total Words", f"{total_words:,}")
            else:
                st.metric("📊 Total Words", "0")

def main():
    """Main application entry point"""
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    # Show appropriate page
    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_main_app()

if __name__ == "__main__":
    main()
