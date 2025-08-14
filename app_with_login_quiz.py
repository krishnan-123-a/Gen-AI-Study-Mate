"""
StudyMate - Complete Version with Login & Quiz System
Professional login system + Interactive quiz functionality
"""

import streamlit as st
import os
import time
import random
from datetime import datetime
import hashlib
import json

# User database (in production, use a real database)
USERS_DB = {
    "admin": {
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
        "name": "Administrator",
        "role": "admin"
    },
    "student": {
        "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",  # "student123"
        "name": "Student User",
        "role": "student"
    },
    "teacher": {
        "password": "8d23cf6c86e834a7aa6eded54c26ce2bb2e74903538c61bdd5d2197997ab2f72",  # "teacher123"
        "name": "Teacher User",
        "role": "teacher"
    }
}

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_login(username, password):
    """Verify user credentials"""
    if username in USERS_DB:
        hashed_password = hash_password(password)
        if USERS_DB[username]["password"] == hashed_password:
            return USERS_DB[username]
    return None

def login_page():
    """Display login page"""
    st.markdown("""
    <style>
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 2rem;
        background: white;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 2px solid #3498db;
    }
    
    .login-header {
        text-align: center;
        margin-bottom: 2rem;
        color: #2c3e50;
    }
    
    .demo-accounts {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .demo-accounts h4 {
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .demo-accounts p {
        color: #6c757d;
        margin: 0.25rem 0;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="login-container">
        <div class="login-header">
            <h1>📚 StudyMate Login</h1>
            <p>AI-Powered Study Companion</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Login form
    with st.form("login_form"):
        st.subheader("🔐 Please Login")
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        login_button = st.form_submit_button("🚀 Login", type="primary")
        
        if login_button:
            if username and password:
                user = verify_login(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.username = username
                    st.success(f"✅ Welcome, {user['name']}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password!")
            else:
                st.warning("⚠️ Please enter both username and password!")
    
    # Demo accounts
    st.markdown("""
    <div class="demo-accounts">
        <h4>🎯 Demo Accounts</h4>
        <p><strong>Admin:</strong> admin / password</p>
        <p><strong>Student:</strong> student / student123</p>
        <p><strong>Teacher:</strong> teacher / teacher123</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features preview
    st.markdown("""
    ### 🌟 StudyMate Features
    - 📁 **PDF Upload & Processing** - Upload study materials
    - 💬 **AI Q&A System** - Ask questions about your documents
    - 🎯 **Interactive Quiz Mode** - Test your knowledge
    - 📊 **Progress Tracking** - Monitor your learning
    - 📝 **Session History** - Review past Q&A sessions
    - 💾 **Export Results** - Download your study sessions
    """)

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
                except Exception as page_error:
                    st.warning(f"Could not extract text from page {page_num + 1}: {str(page_error)}")
                    continue
            
            pdf_document.close()
            
            if text.strip():
                return text.strip()
            else:
                return "No readable text found in this PDF."
                
        except Exception as fitz_error:
            st.error(f"PyMuPDF error: {str(fitz_error)}")
            return None
            
    except ImportError:
        st.error("PyMuPDF is not installed. Please install it with: pip install PyMuPDF")
        return None
    except Exception as e:
        st.error(f"Unexpected error processing PDF: {str(e)}")
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
    
    # Select random chunks for questions
    selected_chunks = random.sample(chunks, min(num_questions, len(chunks)))
    questions = []
    
    quiz_templates = [
        {
            "type": "multiple_choice",
            "question": "Based on the document, what is the main concept discussed in this section?",
            "extract_key": lambda text: text.split('.')[0] if '.' in text else text[:100]
        },
        {
            "type": "true_false",
            "question": "True or False: The following statement is mentioned in the document:",
            "extract_key": lambda text: text.split('.')[0] if '.' in text else text[:100]
        },
        {
            "type": "fill_blank",
            "question": "Fill in the blank based on the document content:",
            "extract_key": lambda text: text.replace(text.split()[len(text.split())//2], "______") if len(text.split()) > 5 else text
        }
    ]
    
    for i, chunk in enumerate(selected_chunks):
        template = random.choice(quiz_templates)
        text = chunk['text']
        
        if template["type"] == "multiple_choice":
            # Extract key concept
            key_concept = template["extract_key"](text)
            
            question = {
                "id": i + 1,
                "type": "multiple_choice",
                "question": f"Q{i+1}: What is the main topic discussed in this excerpt from '{chunk['source']}'?",
                "context": text[:200] + "..." if len(text) > 200 else text,
                "options": [
                    key_concept[:50] + "..." if len(key_concept) > 50 else key_concept,
                    "Unrelated topic A",
                    "Unrelated topic B", 
                    "Unrelated topic C"
                ],
                "correct_answer": 0,
                "source": chunk['source'],
                "explanation": f"This is discussed in the document: {text[:100]}..."
            }
            
        elif template["type"] == "true_false":
            statement = text.split('.')[0] if '.' in text else text[:100]
            
            question = {
                "id": i + 1,
                "type": "true_false",
                "question": f"Q{i+1}: True or False - The following statement is from '{chunk['source']}':",
                "statement": statement,
                "context": text[:200] + "..." if len(text) > 200 else text,
                "correct_answer": True,
                "source": chunk['source'],
                "explanation": f"This statement appears in the document: {chunk['source']}"
            }
            
        else:  # fill_blank
            words = text.split()
            if len(words) > 10:
                blank_word = words[len(words)//2]
                question_text = text.replace(blank_word, "______", 1)
                
                question = {
                    "id": i + 1,
                    "type": "fill_blank",
                    "question": f"Q{i+1}: Fill in the blank from '{chunk['source']}':",
                    "text": question_text[:200] + "..." if len(question_text) > 200 else question_text,
                    "correct_answer": blank_word.lower(),
                    "source": chunk['source'],
                    "explanation": f"The correct word is '{blank_word}' as mentioned in the document."
                }
            else:
                continue
        
        questions.append(question)
    
    return questions

def quiz_mode():
    """Interactive quiz mode"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%); color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; text-align: center;">
        <h1>🎯 Quiz Mode</h1>
        <p>Test your knowledge with AI-generated questions from your study materials</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.chunks:
        st.warning("📁 Please upload PDF documents first to generate quiz questions!")
        return
    
    # Initialize quiz state
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
                    st.error("❌ Could not generate questions. Please upload more content.")
        
        # Show available documents
        if st.session_state.processed_files:
            with st.expander("📚 Available Study Materials"):
                for i, filename in enumerate(st.session_state.processed_files, 1):
                    st.write(f"{i}. {filename}")
    
    # Quiz in progress
    elif st.session_state.quiz_started and not st.session_state.quiz_completed:
        questions = st.session_state.quiz_questions
        current_q = st.session_state.current_question
        
        if current_q < len(questions):
            question = questions[current_q]
            
            # Progress bar
            progress = (current_q + 1) / len(questions)
            st.progress(progress)
            st.write(f"Question {current_q + 1} of {len(questions)}")
            
            # Display question
            st.markdown(f"""
            <div style="background: #f8f9fa; border: 2px solid #3498db; border-radius: 10px; padding: 1.5rem; margin: 1rem 0;">
                <h3>{question['question']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            # Question content based on type
            if question['type'] == 'multiple_choice':
                st.write("**Context:**", question['context'])
                answer = st.radio("Choose the correct answer:", question['options'], key=f"q_{current_q}")
                
            elif question['type'] == 'true_false':
                st.write("**Statement:**", question['statement'])
                st.write("**Context:**", question['context'])
                answer = st.radio("Is this statement true or false?", ["True", "False"], key=f"q_{current_q}")
                
            elif question['type'] == 'fill_blank':
                st.write("**Text:**", question['text'])
                answer = st.text_input("Enter the missing word:", key=f"q_{current_q}")
            
            # Navigation buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if current_q > 0:
                    if st.button("⬅️ Previous"):
                        st.session_state.current_question -= 1
                        st.rerun()
            
            with col2:
                if st.button("💾 Save Answer"):
                    st.session_state.quiz_answers[current_q] = answer
                    st.success("✅ Answer saved!")
            
            with col3:
                if current_q < len(questions) - 1:
                    if st.button("➡️ Next"):
                        st.session_state.quiz_answers[current_q] = answer
                        st.session_state.current_question += 1
                        st.rerun()
                else:
                    if st.button("🏁 Finish Quiz"):
                        st.session_state.quiz_answers[current_q] = answer
                        st.session_state.quiz_completed = True
                        st.rerun()
    
    # Quiz completed
    elif st.session_state.quiz_completed:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%); color: white; padding: 2rem; border-radius: 10px; margin-bottom: 2rem; text-align: center;">
            <h1>🎉 Quiz Completed!</h1>
            <p>Great job! Here are your results:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Calculate score
        questions = st.session_state.quiz_questions
        answers = st.session_state.quiz_answers
        correct_count = 0
        
        for i, question in enumerate(questions):
            user_answer = answers.get(i, "")
            
            if question['type'] == 'multiple_choice':
                if isinstance(user_answer, str) and user_answer == question['options'][question['correct_answer']]:
                    correct_count += 1
            elif question['type'] == 'true_false':
                if (user_answer == "True" and question['correct_answer']) or (user_answer == "False" and not question['correct_answer']):
                    correct_count += 1
            elif question['type'] == 'fill_blank':
                if user_answer.lower().strip() == question['correct_answer'].lower().strip():
                    correct_count += 1
        
        score_percentage = (correct_count / len(questions)) * 100
        
        # Display score
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
        
        # Detailed results
        with st.expander("📋 Detailed Results", expanded=True):
            for i, question in enumerate(questions):
                user_answer = answers.get(i, "No answer")
                
                if question['type'] == 'multiple_choice':
                    correct = user_answer == question['options'][question['correct_answer']]
                    st.write(f"**Q{i+1}:** {question['question']}")
                    st.write(f"**Your answer:** {user_answer}")
                    st.write(f"**Correct answer:** {question['options'][question['correct_answer']]}")
                    
                elif question['type'] == 'true_false':
                    correct = (user_answer == "True" and question['correct_answer']) or (user_answer == "False" and not question['correct_answer'])
                    st.write(f"**Q{i+1}:** {question['question']}")
                    st.write(f"**Statement:** {question['statement']}")
                    st.write(f"**Your answer:** {user_answer}")
                    st.write(f"**Correct answer:** {'True' if question['correct_answer'] else 'False'}")
                    
                elif question['type'] == 'fill_blank':
                    correct = user_answer.lower().strip() == question['correct_answer'].lower().strip()
                    st.write(f"**Q{i+1}:** {question['question']}")
                    st.write(f"**Your answer:** {user_answer}")
                    st.write(f"**Correct answer:** {question['correct_answer']}")
                
                if correct:
                    st.success("✅ Correct!")
                else:
                    st.error("❌ Incorrect")
                    st.info(f"💡 **Explanation:** {question['explanation']}")
                
                st.write("---")
        
        # Quiz actions
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Take New Quiz"):
                # Reset quiz state
                st.session_state.quiz_questions = []
                st.session_state.current_question = 0
                st.session_state.quiz_answers = {}
                st.session_state.quiz_started = False
                st.session_state.quiz_completed = False
                st.rerun()
        
        with col2:
            # Export results
            if st.button("📥 Download Results"):
                results_text = f"StudyMate Quiz Results\n{'='*50}\n\n"
                results_text += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                results_text += f"User: {st.session_state.user['name']}\n"
                results_text += f"Score: {correct_count}/{len(questions)} ({score_percentage:.1f}%)\n\n"
                
                for i, question in enumerate(questions):
                    user_answer = answers.get(i, "No answer")
                    results_text += f"Question {i+1}: {question['question']}\n"
                    results_text += f"Your Answer: {user_answer}\n"
                    
                    if question['type'] == 'multiple_choice':
                        results_text += f"Correct Answer: {question['options'][question['correct_answer']]}\n"
                    elif question['type'] == 'true_false':
                        results_text += f"Correct Answer: {'True' if question['correct_answer'] else 'False'}\n"
                    elif question['type'] == 'fill_blank':
                        results_text += f"Correct Answer: {question['correct_answer']}\n"
                    
                    results_text += f"Source: {question['source']}\n"
                    results_text += "-" * 30 + "\n\n"
                
                st.download_button(
                    label="💾 Save Quiz Results",
                    data=results_text,
                    file_name=f"quiz_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )

def main_app():
    """Main application after login"""
    # Page configuration
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for clear colors
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    
    .main {
        padding: 1rem;
        background-color: #ffffff;
    }
    
    .main-header {
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .main-header h1 {
        color: white !important;
        margin-bottom: 0.5rem;
        font-size: 2.5rem;
    }
    
    .main-header p {
        color: #ecf0f1 !important;
        font-size: 1.2rem;
        margin: 0;
    }
    
    .feature-card {
        background: #ffffff;
        border: 2px solid #e74c3c;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .feature-card h2, .feature-card h3 {
        color: #2c3e50 !important;
        margin-bottom: 1rem;
    }
    
    .feature-card p, .feature-card li {
        color: #34495e !important;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    .user-info {
        background: #d5f4e6;
        border: 2px solid #27ae60;
        color: #1e8449;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'chunks' not in st.session_state:
        st.session_state.chunks = []
    if 'qa_history' not in st.session_state:
        st.session_state.qa_history = []
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = []
    
    # Header with user info
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
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
        
        if st.button("🚪 Logout"):
            # Clear session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["📁 Study Materials", "🎯 Quiz Mode", "📊 Dashboard"])
    
    with tab1:
        # File upload and Q&A (existing functionality)
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
        
        # Process files (simplified version)
        if uploaded_files and len(uploaded_files) != len(st.session_state.processed_files):
            with st.spinner("🔄 Processing PDFs..."):
                all_chunks = []
                processed_files = []
                
                for uploaded_file in uploaded_files:
                    text = extract_text_from_pdf_robust(uploaded_file)
                    if text and len(text.strip()) > 0:
                        chunks = chunk_text_smart(text, uploaded_file.name)
                        if chunks:
                            all_chunks.extend(chunks)
                            processed_files.append(uploaded_file.name)
                
                st.session_state.chunks = all_chunks
                st.session_state.processed_files = processed_files
                
                if all_chunks:
                    st.success(f"✅ Successfully processed {len(processed_files)} PDF(s)!")
        
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
                        # Simple answer generation
                        context = " ".join([chunk['text'] for chunk in relevant_chunks])
                        answer = f"Based on your documents: {context[:500]}..."
                        
                        st.success("✅ Answer generated!")
                        st.write("**Answer:**", answer)
                        
                        sources = list(set(chunk['source'] for chunk in relevant_chunks))
                        st.write("**Sources:**", ", ".join(sources))
                    else:
                        st.warning("🔍 No relevant information found.")
    
    with tab2:
        quiz_mode()
    
    with tab3:
        # Dashboard
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
        
        if st.session_state.processed_files:
            st.subheader("📚 Uploaded Files")
            for i, filename in enumerate(st.session_state.processed_files, 1):
                st.write(f"{i}. {filename}")

def main():
    """Main application entry point"""
    # Check if user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()
