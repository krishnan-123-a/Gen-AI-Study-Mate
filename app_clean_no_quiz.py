"""
StudyMate - Crystal Clear Text Version
Perfect text visibility with high contrast colors
"""

import streamlit as st
import os
import time
import random
from datetime import datetime
import hashlib
import json

# Simple user database
USERS_DB = {
    "admin": {
        "password": "password",
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
    """Verify user credentials"""
    if username in USERS_DB:
        if USERS_DB[username]["password"] == password:
            return USERS_DB[username]
    return None

def show_login_page():
    """Display the login page with crystal clear text"""
    st.set_page_config(
        page_title="StudyMate Login",
        page_icon="📚",
        layout="centered"
    )
    
    # Enhanced CSS with adaptive font colors and dynamic effects
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    /* Light animated gradient background with adaptive text */
    .stApp {
        background: linear-gradient(-45deg, #e3f2fd, #f3e5f5, #fff3e0, #e8f5e8, #fce4ec, #f1f8e9);
        background-size: 400% 400%;
        animation: gradientShift 20s ease infinite;
        color: #2c3e50 !important;
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Light floating particles animation */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle at 20% 80%, rgba(102, 126, 234, 0.08) 2px, transparent 2px),
            radial-gradient(circle at 80% 20%, rgba(118, 75, 162, 0.08) 2px, transparent 2px),
            radial-gradient(circle at 40% 40%, rgba(240, 147, 251, 0.06) 1px, transparent 1px);
        background-size: 120px 120px, 160px 160px, 90px 90px;
        animation: float 25s linear infinite;
        pointer-events: none;
        z-index: 1;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-100px) rotate(360deg); }
    }

    /* Main container with light glassmorphism effect */
    .main {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.8);
        position: relative;
        z-index: 2;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.06);
    }

    /* Light theme login container */
    .login-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        color: #2c3e50 !important;
        padding: 3rem;
        border: 2px solid rgba(102, 126, 234, 0.2);
        border-radius: 25px;
        box-shadow:
            0 20px 40px rgba(0, 0, 0, 0.08),
            0 0 0 1px rgba(255, 255, 255, 0.6),
            inset 0 1px 0 rgba(255, 255, 255, 0.8);
        max-width: 500px;
        margin: 2rem auto;
        text-align: center;
        position: relative;
        z-index: 3;
        animation: slideInUp 0.8s ease-out, lightGlow 3s ease-in-out infinite alternate;
        transition: all 0.3s ease;
    }

    .login-container:hover {
        transform: translateY(-5px);
        box-shadow:
            0 30px 60px rgba(0, 0, 0, 0.15),
            0 0 0 1px rgba(255, 255, 255, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }

    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(50px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes lightGlow {
        from {
            box-shadow:
                0 20px 40px rgba(0, 0, 0, 0.08),
                0 0 15px rgba(102, 126, 234, 0.15);
        }
        to {
            box-shadow:
                0 20px 40px rgba(0, 0, 0, 0.08),
                0 0 25px rgba(118, 75, 162, 0.2);
        }
    }
    
    /* Light theme login title */
    .login-title {
        background: linear-gradient(45deg, #667eea, #764ba2, #2c3e50);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
        font-weight: 700 !important;
        text-align: center;
        animation: textShine 4s ease-in-out infinite alternate, lightBounce 3s ease-in-out infinite;
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
        position: relative;
    }

    /* Fallback for browsers that don't support background-clip */
    .login-title::after {
        content: attr(data-text);
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        color: #2c3e50;
        z-index: -1;
    }

    @keyframes textShine {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes lightBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); }
    }

    .login-subtitle {
        color: #2c3e50 !important;
        font-size: 1.2rem !important;
        margin-bottom: 2rem !important;
        font-weight: 500 !important;
        animation: fadeInUp 1s ease-out 0.3s both;
        opacity: 0.9;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 0.8;
            transform: translateY(0);
        }
    }
    
    /* Interactive demo accounts section with card effects */
    .demo-accounts {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: left;
        animation: slideInLeft 0.8s ease-out 0.5s both;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .demo-accounts:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        border-color: rgba(102, 126, 234, 0.5);
    }

    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .demo-accounts h3 {
        color: #1a1a1a !important;
        margin-bottom: 1.5rem !important;
        text-align: center !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        position: relative;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    .demo-accounts h3::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
        width: 50px;
        height: 3px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 2px;
    }

    .demo-account {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #1a1a1a !important;
        padding: 1.5rem;
        border: 2px solid transparent;
        border-radius: 15px;
        margin: 1rem 0;
        font-family: 'Poppins', sans-serif;
        font-size: 1rem !important;
        font-weight: 500 !important;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
        text-shadow: 0 1px 1px rgba(255, 255, 255, 0.9);
    }

    .demo-account::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: left 0.5s ease;
    }

    .demo-account:hover {
        transform: translateY(-2px) scale(1.02);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }

    .demo-account:hover::before {
        left: 100%;
    }
    
    /* Features section */
    .features-list {
        background-color: #f0f8f0 !important;
        border: 2px solid #000000 !important;
        border-radius: 10px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: left;
    }
    
    .features-list h3 {
        color: #2c3e50 !important;
        margin-bottom: 1rem !important;
        text-align: center !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
    }

    .features-list ul {
        color: #444444 !important;
        margin: 0;
        padding-left: 2rem;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }

    .features-list li {
        color: #444444 !important;
        margin: 0.5rem 0 !important;
        font-weight: 400 !important;
    }
    
    /* Override all Streamlit text colors */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown div, .stMarkdown span {
        color: #444444 !important;
        font-weight: 400 !important;
    }

    /* Form elements */
    .stTextInput label, .stSelectbox label, .stButton label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Input fields */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #444444 !important;
        border: 2px solid #cccccc !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
    }

    /* Interactive buttons with animations and effects */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 1rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        font-family: 'Poppins', sans-serif;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        cursor: pointer;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .stButton button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s ease;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        color: #ffffff !important;
    }

    .stButton button:hover::before {
        left: 100%;
    }

    .stButton button:active {
        transform: translateY(-1px) scale(1.02);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }

    /* Special styling for primary buttons */
    .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);
        animation: pulse 2s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% {
            box-shadow: 0 8px 20px rgba(240, 147, 251, 0.4);
        }
        50% {
            box-shadow: 0 12px 30px rgba(240, 147, 251, 0.6);
        }
    }

    .stButton button[kind="primary"]:hover {
        background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
        box-shadow: 0 15px 35px rgba(240, 147, 251, 0.5);
    }
    
    /* Success/Error messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        color: #444444 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }

    /* Ensure all text is visible but not too bold */
    * {
        color: #444444 !important;
        font-weight: 400 !important;
    }

    /* Override any inherited colors */
    div, p, span, h1, h2, h3, h4, h5, h6, label, text {
        color: #444444 !important;
        font-weight: 400 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main login container with enhanced contrast
    st.markdown("""
    <div class="login-container">
        <h1 class="login-title" data-text="📚 StudyMate">📚 StudyMate</h1>
        <p class="login-subtitle">AI-Powered Study Companion</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Login section header
    st.markdown("## 🔐 Login to Continue")
    st.markdown("#### Choose your login method below:")
    
    # Quick login buttons section
    st.markdown("### 🚀 Quick Login (Recommended)")
    st.markdown("**Click any button below for instant access:**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👑 Admin Login", use_container_width=True, type="primary"):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["admin"]
            st.session_state.username = "admin"
            st.success("✅ Logged in as Administrator!")
            st.balloons()
            time.sleep(1)
            st.rerun()
    
    with col2:
        if st.button("🎓 Student Login", use_container_width=True, type="primary"):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["student"]
            st.session_state.username = "student"
            st.success("✅ Logged in as Student!")
            st.balloons()
            time.sleep(1)
            st.rerun()
    
    with col3:
        if st.button("👨‍🏫 Teacher Login", use_container_width=True, type="primary"):
            st.session_state.logged_in = True
            st.session_state.user = USERS_DB["teacher"]
            st.session_state.username = "teacher"
            st.success("✅ Logged in as Teacher!")
            st.balloons()
            time.sleep(1)
            st.rerun()
    
    st.markdown("---")
    
    # Manual login form
    st.markdown("### 📝 Manual Login Form")
    st.markdown("**Or enter credentials manually:**")
    
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "👤 Username", 
            placeholder="Enter username (admin, student, or teacher)",
            help="Use one of the demo accounts"
        )
        password = st.text_input(
            "🔒 Password", 
            type="password",
            placeholder="Enter password",
            help="Use the corresponding password"
        )
        
        login_clicked = st.form_submit_button(
            "🚀 Login Now", 
            type="primary",
            use_container_width=True
        )
        
        if login_clicked:
            if username and password:
                user = verify_login(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.username = username
                    st.success(f"✅ Welcome, {user['name']}!")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password!")
            else:
                st.warning("⚠️ Please enter both username and password!")
    
    # Demo accounts info
    st.markdown("""
    <div class="demo-accounts">
        <h3>🎯 Demo Account Credentials</h3>
        <div class="demo-account">
            <strong>👑 Administrator:</strong><br>
            Username: admin<br>
            Password: password
        </div>
        <div class="demo-account">
            <strong>🎓 Student:</strong><br>
            Username: student<br>
            Password: student123
        </div>
        <div class="demo-account">
            <strong>👨‍🏫 Teacher:</strong><br>
            Username: teacher<br>
            Password: teacher123
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Features preview
    st.markdown("""
    <div class="features-list">
        <h3>🌟 StudyMate Features</h3>
        <ul>
            <li>📁 <strong>PDF Upload & Processing</strong> - Upload and analyze study materials</li>
            <li>💬 <strong>AI Q&A System</strong> - Ask questions about your documents</li>
            <li>🎯 <strong>Interactive Quiz Mode</strong> - Test knowledge with AI-generated questions</li>
            <li>📊 <strong>Progress Tracking</strong> - Monitor your learning progress</li>
            <li>📝 <strong>Session History</strong> - Review past Q&A sessions</li>
            <li>💾 <strong>Export Results</strong> - Download study sessions and quiz results</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

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
    """Generate intelligent quiz questions from educational content with subject-specific templates"""
    if not chunks or len(chunks) < num_questions:
        return []

    selected_chunks = random.sample(chunks, min(num_questions, len(chunks)))
    questions = []

    # Comprehensive question templates for different educational subjects
    question_templates = [
        # Mathematics Templates
        {
            "pattern": ["algebra", "equation", "variable", "solve", "linear", "quadratic"],
            "question": "What mathematical concept is explained in this section?",
            "correct_option": "Algebraic equations and problem solving",
            "wrong_options": ["Chemical reaction mechanisms", "Historical timeline analysis", "Literary character development"]
        },
        {
            "pattern": ["geometry", "triangle", "circle", "area", "volume", "pythagorean"],
            "question": "What geometric principle is discussed here?",
            "correct_option": "Geometric shapes and spatial relationships",
            "wrong_options": ["Biological cell structures", "Economic market trends", "Programming data structures"]
        },
        {
            "pattern": ["calculus", "derivative", "integral", "limit", "function"],
            "question": "What calculus concept is being explained?",
            "correct_option": "Calculus and mathematical analysis",
            "wrong_options": ["Physics wave properties", "Historical cause and effect", "Literary narrative techniques"]
        },

        # Science Templates
        {
            "pattern": ["physics", "force", "energy", "motion", "newton", "gravity"],
            "question": "What physics principle is described in this content?",
            "correct_option": "Physical laws and natural phenomena",
            "wrong_options": ["Mathematical algebraic concepts", "Historical political systems", "Literary writing techniques"]
        },
        {
            "pattern": ["chemistry", "atom", "molecule", "reaction", "element", "periodic"],
            "question": "What chemistry concept is explained here?",
            "correct_option": "Chemical properties and reactions",
            "wrong_options": ["Geometric measurement formulas", "Historical cultural movements", "Programming algorithms"]
        },
        {
            "pattern": ["biology", "cell", "organism", "evolution", "dna", "ecosystem"],
            "question": "What biological concept is discussed in this section?",
            "correct_option": "Living organisms and life processes",
            "wrong_options": ["Mathematical statistical analysis", "Historical timeline events", "Computer system architecture"]
        },

        # History Templates
        {
            "pattern": ["civilization", "empire", "ancient", "medieval", "war", "revolution"],
            "question": "What historical period or event is described here?",
            "correct_option": "Historical events and civilizations",
            "wrong_options": ["Mathematical problem-solving methods", "Scientific experimental procedures", "Programming language syntax"]
        },
        {
            "pattern": ["democracy", "government", "political", "society", "culture", "social"],
            "question": "What social or political concept is explained in this content?",
            "correct_option": "Political systems and social structures",
            "wrong_options": ["Chemical bonding theories", "Geometric proof methods", "Computer network protocols"]
        },

        # Literature Templates
        {
            "pattern": ["literature", "poetry", "novel", "character", "plot", "theme"],
            "question": "What literary element or concept is discussed here?",
            "correct_option": "Literary analysis and writing techniques",
            "wrong_options": ["Mathematical equation solving", "Scientific hypothesis testing", "Historical chronological analysis"]
        },
        {
            "pattern": ["writing", "grammar", "sentence", "paragraph", "essay", "language"],
            "question": "What language arts concept is explained in this section?",
            "correct_option": "Language structure and communication skills",
            "wrong_options": ["Physics motion calculations", "Chemical formula balancing", "Computer programming logic"]
        },

        # Computer Science Templates
        {
            "pattern": ["programming", "code", "algorithm", "software", "computer", "data"],
            "question": "What computer science concept is described here?",
            "correct_option": "Programming and computational thinking",
            "wrong_options": ["Historical document analysis", "Literary metaphor interpretation", "Mathematical geometric proofs"]
        },
        {
            "pattern": ["network", "internet", "database", "security", "web", "system"],
            "question": "What technology concept is explained in this content?",
            "correct_option": "Computer systems and digital technology",
            "wrong_options": ["Biological ecosystem relationships", "Historical cause-effect patterns", "Literary narrative structures"]
        },

        # Machine Learning (from original)
        {
            "pattern": ["machine learning", "ml", "artificial intelligence", "ai", "neural"],
            "question": "What artificial intelligence concept is discussed here?",
            "correct_option": "Machine learning and AI technologies",
            "wrong_options": ["Historical political movements", "Literary character analysis", "Mathematical geometric principles"]
        },

        # Programming Language Specific Templates
        {
            "pattern": ["python", "def", "import", "class", "list", "dictionary"],
            "question": "What Python programming concept is explained in this section?",
            "correct_option": "Python syntax and programming fundamentals",
            "wrong_options": ["JavaScript DOM manipulation", "HTML markup structure", "CSS styling properties"]
        },
        {
            "pattern": ["javascript", "function", "var", "let", "const", "dom", "event"],
            "question": "What JavaScript concept is described here?",
            "correct_option": "JavaScript programming and web development",
            "wrong_options": ["Python data structures", "Mathematical calculus", "Historical timeline events"]
        },
        {
            "pattern": ["html", "tag", "element", "attribute", "markup", "semantic"],
            "question": "What web development concept is discussed in this content?",
            "correct_option": "HTML structure and web markup",
            "wrong_options": ["Python object-oriented programming", "Mathematical algebra", "Scientific chemistry"]
        },
        {
            "pattern": ["css", "selector", "property", "style", "layout", "responsive"],
            "question": "What CSS concept is explained here?",
            "correct_option": "CSS styling and web design",
            "wrong_options": ["JavaScript event handling", "Python data analysis", "Historical political systems"]
        },
        {
            "pattern": ["variable", "function", "loop", "condition", "array", "object"],
            "question": "What programming concept is described in this section?",
            "correct_option": "Programming fundamentals and logic",
            "wrong_options": ["Literary narrative techniques", "Historical cause-effect analysis", "Mathematical geometric proofs"]
        },
        {
            "pattern": ["syntax", "code", "programming", "development", "software", "application"],
            "question": "What software development concept is discussed here?",
            "correct_option": "Software development and programming practices",
            "wrong_options": ["Biological ecosystem relationships", "Literary character development", "Mathematical statistical analysis"]
        },
        {
            "pattern": ["web", "frontend", "backend", "server", "client", "api"],
            "question": "What web development architecture concept is explained here?",
            "correct_option": "Web development architecture and design",
            "wrong_options": ["Chemical molecular structures", "Historical social movements", "Literary plot structures"]
        },
        {
            "pattern": ["database", "sql", "query", "table", "data", "storage"],
            "question": "What database concept is described in this content?",
            "correct_option": "Database management and data storage",
            "wrong_options": ["Physics motion calculations", "Literary metaphor analysis", "Historical document interpretation"]
        }
    ]

    for i, chunk in enumerate(selected_chunks):
        text = chunk['text'].lower()

        # Find the best matching template
        best_template = None
        max_matches = 0

        for template in question_templates:
            matches = sum(1 for pattern in template["pattern"] if pattern in text)
            if matches > max_matches:
                max_matches = matches
                best_template = template

        # Use best template or default
        if best_template and max_matches > 0:
            question_text = f"Q{i+1}: {best_template['question']}"
            correct_option = best_template['correct_option']
            wrong_options = best_template['wrong_options']
        else:
            # Default question for general content
            question_text = f"Q{i+1}: What is the main topic discussed in this excerpt?"
            correct_option = "The concept described in the provided text"
            wrong_options = ["Database management systems", "Web development frameworks", "Network security protocols"]

        # Randomize option positions
        options = [correct_option] + wrong_options
        correct_answer_index = 0

        # Shuffle options and track correct answer
        shuffled_options = options.copy()
        random.shuffle(shuffled_options)
        correct_answer_index = shuffled_options.index(correct_option)

        question = {
            "id": i + 1,
            "type": "multiple_choice",
            "question": question_text,
            "context": chunk['text'][:300] + "..." if len(chunk['text']) > 300 else chunk['text'],
            "options": shuffled_options,
            "correct_answer": correct_answer_index,
            "source": chunk['source'],
            "explanation": f"Based on the content from '{chunk['source']}', this topic is clearly discussed in the provided excerpt.",
            "chunk_preview": chunk['text'][:150] + "..." if len(chunk['text']) > 150 else chunk['text']
        }

        questions.append(question)

    return questions

def show_main_app():
    """Main application with crystal clear text"""
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        page_icon="📚",
        layout="wide"
    )
    
    # Enhanced CSS for interactive main app with animations
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    /* Light animated gradient background for main app */
    .stApp {
        background: linear-gradient(-45deg, #e3f2fd, #f3e5f5, #fff3e0, #e8f5e8, #fce4ec, #f1f8e9);
        background-size: 400% 400%;
        animation: gradientShift 25s ease infinite;
        color: #2c3e50 !important;
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Light floating particles for main app */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle at 25% 25%, rgba(102, 126, 234, 0.06) 2px, transparent 2px),
            radial-gradient(circle at 75% 75%, rgba(118, 75, 162, 0.06) 1px, transparent 1px);
        background-size: 130px 130px, 90px 90px;
        animation: floatParticles 30s linear infinite;
        pointer-events: none;
        z-index: 1;
    }

    @keyframes floatParticles {
        0% { transform: translateY(0px) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }

    .main {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.9);
        padding: 1rem;
        position: relative;
        z-index: 2;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.05);
    }

    /* Light theme header with subtle gradient */
    .main-header {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 50%, #fff3e0 100%);
        background-size: 200% 200%;
        animation: headerGradient 12s ease infinite;
        color: #2c3e50 !important;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        border: 2px solid rgba(102, 126, 234, 0.2);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06);
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }

    @keyframes headerGradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
        pointer-events: none;
    }

    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .main-header:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
    }
    
    .main-header h1 {
        color: #ffffff !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.8rem !important;
        font-weight: 500 !important;
    }

    .main-header p {
        color: #ffffff !important;
        font-size: 1rem !important;
        margin: 0 !important;
    }
    
    /* User info box */
    .user-info {
        background-color: #d4edda !important;
        border: 2px solid #28a745 !important;
        color: #2c3e50 !important;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 500 !important;
        text-align: center;
        font-size: 1rem !important;
    }
    
    /* Interactive feature cards with hover effects */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(0, 123, 255, 0.3);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
        animation: slideInUp 0.6s ease-out;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 123, 255, 0.1), transparent);
        transition: left 0.6s ease;
    }

    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(0, 123, 255, 0.6);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
    }

    .feature-card:hover::before {
        left: 100%;
    }

    .feature-card h2, .feature-card h3 {
        color: #1a1a1a !important;
        margin-bottom: 1.5rem !important;
        font-weight: 600 !important;
        position: relative;
        animation: fadeInDown 0.8s ease-out 0.2s both;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    .feature-card h2::after, .feature-card h3::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 0;
        height: 3px;
        background: linear-gradient(45deg, #007bff, #6f42c1);
        border-radius: 2px;
        transition: width 0.4s ease;
    }

    .feature-card:hover h2::after, .feature-card:hover h3::after {
        width: 60px;
    }

    .feature-card p {
        color: #2c3e50 !important;
        font-size: 1rem !important;
        line-height: 1.8 !important;
        font-weight: 400 !important;
        animation: fadeInUp 0.8s ease-out 0.4s both;
        opacity: 0.95;
        text-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);
    }

    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 0.9;
            transform: translateY(0);
        }
    }
    
    /* Quiz container */
    .quiz-container {
        background-color: #f8f9fa !important;
        border: 3px solid #17a2b8 !important;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    .quiz-container h1, .quiz-container h2, .quiz-container h3 {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }

    .quiz-container p {
        color: #555555 !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
    }
    
    /* Override all text colors */
    .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown div, .stMarkdown span,
    .stText, .stWrite {
        color: #555555 !important;
        font-weight: 400 !important;
    }

    /* Form elements */
    .stTextInput label, .stSelectbox label, .stFileUploader label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }

    /* Input fields */
    .stTextInput input, .stSelectbox select {
        background-color: #ffffff !important;
        color: #444444 !important;
        border: 2px solid #cccccc !important;
        font-size: 1rem !important;
        font-weight: 400 !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #3498db !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }

    .stButton button:hover {
        background-color: #2980b9 !important;
        color: #ffffff !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: #2c3e50 !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Metrics */
    .metric-container {
        background-color: #ffffff !important;
        border: 2px solid #333333 !important;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
    
    /* Ensure all text is readable but not too bold */
    * {
        color: #555555 !important;
        font-weight: 400 !important;
    }

    /* Force override any inherited styles */
    div, p, span, h1, h2, h3, h4, h5, h6, label, text, strong, em {
        color: #555555 !important;
        font-weight: 400 !important;
    }

    /* Headings optimized for light background */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    /* Headings inside containers */
    .stContainer h1, .stContainer h2, .stContainer h3,
    .stContainer h4, .stContainer h5, .stContainer h6,
    .feature-card h1, .feature-card h2, .feature-card h3,
    .feature-card h4, .feature-card h5, .feature-card h6 {
        color: #2c3e50 !important;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
    }

    /* Interactive loading animations */
    .loading-dots {
        display: inline-block;
        animation: loadingDots 1.5s infinite;
    }

    @keyframes loadingDots {
        0%, 20% { opacity: 0; }
        50% { opacity: 1; }
        80%, 100% { opacity: 0; }
    }

    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #667eea, #764ba2);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #764ba2, #667eea);
    }

    /* Tooltip animations */
    .tooltip {
        position: relative;
        cursor: help;
    }

    .tooltip::after {
        content: attr(data-tooltip);
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        white-space: nowrap;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 1000;
    }

    .tooltip:hover::after {
        opacity: 1;
        visibility: visible;
        transform: translateX(-50%) translateY(-5px);
    }
    </style>

    <script>
    // Add interactive cursor effects
    document.addEventListener('DOMContentLoaded', function() {
        // Create cursor follower
        const cursor = document.createElement('div');
        cursor.className = 'cursor-follower';
        cursor.style.cssText = `
            position: fixed;
            width: 20px;
            height: 20px;
            background: radial-gradient(circle, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.4));
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            transition: transform 0.1s ease;
            mix-blend-mode: difference;
        `;
        document.body.appendChild(cursor);

        // Update cursor position
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX - 10 + 'px';
            cursor.style.top = e.clientY - 10 + 'px';
        });

        // Add click ripple effect
        document.addEventListener('click', (e) => {
            const ripple = document.createElement('div');
            ripple.style.cssText = `
                position: fixed;
                width: 0;
                height: 0;
                border-radius: 50%;
                background: radial-gradient(circle, rgba(102, 126, 234, 0.6), transparent);
                pointer-events: none;
                z-index: 9998;
                left: ${e.clientX}px;
                top: ${e.clientY}px;
                transform: translate(-50%, -50%);
                animation: rippleEffect 0.6s ease-out forwards;
            `;

            const style = document.createElement('style');
            style.textContent = `
                @keyframes rippleEffect {
                    to {
                        width: 100px;
                        height: 100px;
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
            document.body.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
                style.remove();
            }, 600);
        });

        // Add parallax effect to background elements
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.stApp::before');
            if (parallax) {
                parallax.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
        });
    });
    </script>
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
        
        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Navigation tabs
    tab1, tab2, tab3 = st.tabs(["📁 Study Materials", "🎯 Quiz Mode", "📊 Dashboard"])
    
    with tab1:
        st.markdown("""
        <div class="feature-card">
            <h2>📁 Upload Study Materials</h2>
            <p>Upload your PDF study materials to get started with AI-powered Q&A and quiz generation.</p>
            <p><strong>🎓 Educational PDFs Available:</strong> Mathematics, Science, History, Literature, Computer Science</p>
            <p><strong>📚 Perfect for:</strong> Students, Teachers, Self-Study, Exam Preparation</p>
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
                            st.success(f"✅ Successfully processed: {uploaded_file.name}")
                
                st.session_state.chunks = all_chunks
                st.session_state.processed_files = processed_files
                
                if all_chunks:
                    st.balloons()
                    st.success(f"🎉 Successfully processed {len(processed_files)} PDF(s) into {len(all_chunks)} text chunks!")
        
        # Q&A Interface
        if st.session_state.chunks:
            st.markdown("""
            <div class="feature-card">
                <h2>💬 Ask Questions About Your Documents</h2>
                <p>Ask any question about your uploaded study materials and get AI-powered answers.</p>
            </div>
            """, unsafe_allow_html=True)
            
            query = st.text_input(
                "Your Question:",
                placeholder="e.g., What is machine learning and how does it work?",
                help="Ask any question about your uploaded documents"
            )
            
            if st.button("🔍 Get Answer", type="primary") and query:
                with st.spinner("🤖 Analyzing documents and generating answer..."):
                    relevant_chunks = advanced_search(query, st.session_state.chunks)
                    
                    if relevant_chunks:
                        context = " ".join([chunk['text'] for chunk in relevant_chunks])
                        answer = f"Based on your uploaded documents: {context[:500]}..."
                        
                        st.success("✅ Answer generated successfully!")
                        st.markdown("#### 💡 Answer:")
                        st.write(answer)

                        sources = list(set(chunk['source'] for chunk in relevant_chunks))
                        st.markdown("#### 📚 Sources:")
                        st.write(", ".join(sources))
                    else:
                        st.warning("🔍 No relevant information found in your documents.")
        else:
            st.info("📁 Please upload PDF documents to get started with Q&A and quiz features.")
    
    with tab2:
        st.markdown("""
        <div class="quiz-container">
            <h1>🎯 Interactive Quiz Mode</h1>
            <p><strong>AI-Generated Educational Quizzes from Your PDFs</strong></p>
            <p>✅ Questions automatically created from your uploaded documents<br>
            ✅ 4 multiple-choice options per question<br>
            ✅ One correct answer based on your PDF content<br>
            ✅ Subject-specific question generation for all educational topics</p>
            <p><strong>📚 Supported Subjects:</strong> Mathematics, Science, History, Literature, Computer Science, and more!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.chunks:
            st.warning("📁 Please upload PDF documents first to generate quiz questions!")

            # Show interactive sample questions when no PDFs are uploaded
            st.markdown("### 🎯 Interactive Sample Quiz Questions")
            st.info("Here are examples of the types of questions AI will generate from your PDFs. Try answering them!")

            # Initialize sample quiz state
            if 'sample_answers' not in st.session_state:
                st.session_state.sample_answers = {}
            if 'sample_submitted' not in st.session_state:
                st.session_state.sample_submitted = {}

            # Sample questions for different subjects
            sample_questions = [
                {
                    "subject": "📊 Mathematics",
                    "question": "What mathematical concept is explained in this section?",
                    "context": "A linear equation is an equation that makes a straight line when graphed. The standard form is y = mx + b, where m is the slope and b is the y-intercept.",
                    "options": [
                        "✅ Algebraic equations and problem solving",
                        "○ Chemical reaction mechanisms",
                        "○ Historical timeline analysis",
                        "○ Literary character development"
                    ],
                    "explanation": "This question tests understanding of linear equations, a fundamental algebraic concept."
                },
                {
                    "subject": "🔬 Science",
                    "question": "What physics principle is described in this content?",
                    "context": "Newton's First Law states that an object at rest stays at rest, and an object in motion stays in motion, unless acted upon by an external force.",
                    "options": [
                        "✅ Physical laws and natural phenomena",
                        "○ Mathematical algebraic concepts",
                        "○ Historical political systems",
                        "○ Literary writing techniques"
                    ],
                    "explanation": "This question focuses on Newton's laws of motion, fundamental principles in physics."
                },
                {
                    "subject": "🏛️ History",
                    "question": "What historical period is described here?",
                    "context": "The Renaissance was a 'rebirth' of classical learning and culture, characterized by humanism and artistic innovation during the 14th-17th centuries.",
                    "options": [
                        "✅ Historical events and civilizations",
                        "○ Mathematical problem-solving methods",
                        "○ Scientific experimental procedures",
                        "○ Programming language syntax"
                    ],
                    "explanation": "This question tests knowledge of the Renaissance period, a major era in European history."
                },
                {
                    "subject": "📖 Literature",
                    "question": "What literary element is discussed in this section?",
                    "context": "A metaphor is a direct comparison between two unlike things without using 'like' or 'as'. It creates vivid imagery by stating one thing is another.",
                    "options": [
                        "✅ Literary analysis and writing techniques",
                        "○ Physics motion calculations",
                        "○ Chemical formula balancing",
                        "○ Computer programming logic"
                    ],
                    "explanation": "This question focuses on literary devices, specifically metaphors used in writing and analysis."
                },
                {
                    "subject": "💻 Computer Science",
                    "question": "What computer science concept is described here?",
                    "context": "An algorithm is a step-by-step procedure for solving a problem. It must be precise, unambiguous, and finite to be executed by a computer.",
                    "options": [
                        "✅ Programming and computational thinking",
                        "○ Historical document analysis",
                        "○ Literary metaphor interpretation",
                        "○ Mathematical geometric proofs"
                    ],
                    "explanation": "This question tests understanding of algorithms, fundamental concepts in computer science."
                }
            ]

            # Display interactive sample questions
            for i, sample in enumerate(sample_questions, 1):
                # Create interactive question card
                st.markdown(f"""
                <div style="
                    background: rgba(255, 255, 255, 0.95);
                    backdrop-filter: blur(20px);
                    border: 2px solid rgba(102, 126, 234, 0.3);
                    border-radius: 20px;
                    padding: 2rem;
                    margin: 1.5rem 0;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                    animation: questionSlideIn 0.6s ease-out;
                ">
                    <div style="
                        background: linear-gradient(45deg, #667eea, #764ba2);
                        color: white;
                        padding: 1rem;
                        border-radius: 15px;
                        margin-bottom: 1.5rem;
                        text-align: center;
                    ">
                        <h3 style="margin: 0; color: white;">📝 Sample Question {i}: {sample['subject']}</h3>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Question content
                st.markdown(f"**Question:** {sample['question']}")

                # Source and context
                st.markdown(f"**📄 Source:** Sample_{sample['subject'].replace(' ', '_')}.pdf")
                st.markdown("**📖 Context from PDF:**")
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                    border-left: 6px solid #667eea;
                    border-radius: 10px;
                    padding: 1rem;
                    margin: 1rem 0;
                    font-style: italic;
                    color: #2c3e50;
                ">
                    {sample['context']}
                </div>
                """, unsafe_allow_html=True)

                # Interactive answer options
                st.markdown("**🎯 Choose your answer:**")

                # Clean options for radio button (remove ✅ and ○ symbols)
                clean_options = []
                correct_index = -1
                for j, option in enumerate(sample['options']):
                    if option.startswith("✅"):
                        clean_option = option.replace("✅ ", "")
                        correct_index = j
                    else:
                        clean_option = option.replace("○ ", "")
                    clean_options.append(clean_option)

                # Radio button for answers
                user_answer = st.radio(
                    f"Select your answer for Question {i}:",
                    clean_options,
                    key=f"sample_q_{i}",
                    index=None
                )

                # Submit button for each question
                col1, col2 = st.columns([1, 3])
                with col1:
                    if st.button(f"Submit Answer {i}", key=f"submit_{i}"):
                        if user_answer:
                            st.session_state.sample_answers[i] = user_answer
                            st.session_state.sample_submitted[i] = True
                            st.rerun()
                        else:
                            st.warning("Please select an answer first!")

                # Show result if submitted
                if st.session_state.sample_submitted.get(i, False):
                    user_answer = st.session_state.sample_answers.get(i, "")
                    correct_answer = clean_options[correct_index]
                    is_correct = user_answer == correct_answer

                    if is_correct:
                        st.success(f"✅ Correct! You selected: {user_answer}")
                        st.balloons()
                    else:
                        st.error(f"❌ Incorrect. You selected: {user_answer}")
                        st.info(f"✅ Correct answer: {correct_answer}")

                    # Show explanation
                    st.markdown("**💡 Explanation:**")
                    st.info(sample['explanation'])

                    # Reset button
                    if st.button(f"Try Again {i}", key=f"reset_{i}"):
                        if i in st.session_state.sample_answers:
                            del st.session_state.sample_answers[i]
                        if i in st.session_state.sample_submitted:
                            del st.session_state.sample_submitted[i]
                        st.rerun()

                st.markdown("---")

            st.markdown("---")
            st.markdown("### 🎓 Educational Benefits")

            col_edu1, col_edu2 = st.columns(2)
            with col_edu1:
                st.markdown("""
                **✅ For Students:**
                • Test understanding immediately
                • Practice with your own materials
                • Get instant feedback
                • Track learning progress
                • Prepare for exams effectively
                """)
            with col_edu2:
                st.markdown("""
                **✅ For Teachers:**
                • Generate quizzes instantly
                • Assess student comprehension
                • Save time on question creation
                • Use any educational content
                • Track class performance
                """)

            st.markdown("### 🚀 Ready to Create Your Own Quiz?")
            st.info("Upload your PDF study materials in the 'Study Materials' tab to generate personalized quiz questions!")

            # Show available educational PDFs
            st.markdown("### 📚 Educational PDFs Available for Testing:")
            educational_pdfs = [
                "📊 Mathematics_Fundamentals.pdf - Algebra, Geometry, Calculus",
                "🔬 Science_Fundamentals.pdf - Physics, Chemistry, Biology",
                "🏛️ World_History_Overview.pdf - Ancient to Modern History",
                "📖 Literature_Language_Arts.pdf - Literary Analysis & Writing",
                "💻 Computer_Science_Fundamentals.pdf - Programming & Technology",
                "🐍 Python_Programming_Guide.pdf - Python Syntax & Concepts",
                "🌐 JavaScript_Programming_Guide.pdf - JavaScript & Web Development",
                "🌐 Web_Development_Guide.pdf - HTML, CSS, Frontend/Backend",
                "🤖 ML_Demo_for_Quiz.pdf - Machine Learning & AI Concepts"
            ]

            for pdf in educational_pdfs:
                st.markdown(f"• {pdf}")

            st.success("💡 **Tip:** Upload any of these PDFs to see subject-specific quiz generation in action!")

        else:
            # Quiz setup
            if not st.session_state.quiz_started:
                st.markdown("### 🎮 Quiz Setup")
                st.info("🤖 **How it works:** AI will analyze your uploaded PDFs and automatically generate multiple-choice questions with 4 options each. One option will be correct based on your document content!")

                # Show what types of questions will be generated
                st.markdown("#### 🎯 Questions Generated from Your PDFs:")

                # Display available documents and preview questions they'll generate
                if st.session_state.processed_files:
                    st.markdown("#### 📚 Your Uploaded Documents & Question Types:")

                    for filename in st.session_state.processed_files:
                        # Create expandable preview for each document
                        with st.expander(f"📄 {filename} - Preview Questions"):
                            if "Mathematics" in filename:
                                st.markdown("📊 **Mathematics Questions:** Algebra, Geometry, Calculus concepts")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What mathematical concept is explained in this section about linear equations?")
                                st.markdown("**Options:** A) Algebraic equations B) Chemical reactions C) Historical events D) Literary themes")

                            elif "Science" in filename:
                                st.markdown("🔬 **Science Questions:** Physics, Chemistry, Biology principles")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What physics principle is described in this content about Newton's laws?")
                                st.markdown("**Options:** A) Physical laws B) Mathematical concepts C) Historical systems D) Literary techniques")

                            elif "History" in filename:
                                st.markdown("🏛️ **History Questions:** Historical events, periods, civilizations")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What historical period is described in this section about the Renaissance?")
                                st.markdown("**Options:** A) Historical events B) Scientific procedures C) Programming syntax D) Mathematical methods")

                            elif "Literature" in filename:
                                st.markdown("📖 **Literature Questions:** Literary elements, writing techniques")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What literary element is discussed in this section about metaphors?")
                                st.markdown("**Options:** A) Literary techniques B) Physics calculations C) Chemical formulas D) Programming logic")

                            elif "Computer" in filename:
                                st.markdown("💻 **Computer Science Questions:** Programming, algorithms, technology")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What computer science concept is described in this content about algorithms?")
                                st.markdown("**Options:** A) Programming concepts B) Historical analysis C) Literary interpretation D) Mathematical proofs")

                            elif "Python" in filename:
                                st.markdown("🐍 **Python Questions:** Syntax, data structures, object-oriented programming")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What Python programming concept is explained in this section about lists?")
                                st.markdown("**Options:** A) Python fundamentals B) JavaScript DOM C) HTML structure D) CSS properties")

                            elif "JavaScript" in filename:
                                st.markdown("🌐 **JavaScript Questions:** Functions, DOM manipulation, web development")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What JavaScript concept is described in this content about functions?")
                                st.markdown("**Options:** A) JavaScript programming B) Python data structures C) Mathematical calculus D) Historical events")

                            elif "Web" in filename:
                                st.markdown("🌐 **Web Development Questions:** HTML, CSS, frontend/backend concepts")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What web development concept is discussed in this content about HTML?")
                                st.markdown("**Options:** A) HTML structure B) Python OOP C) Mathematical algebra D) Scientific chemistry")

                            elif "ML" in filename or "Machine" in filename:
                                st.markdown("🤖 **AI/ML Questions:** Machine learning, neural networks, algorithms")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What machine learning concept is explained in this section?")
                                st.markdown("**Options:** A) ML algorithms B) Historical movements C) Literary analysis D) Mathematical principles")

                            else:
                                st.markdown(f"📄 **{filename}:** Subject-specific questions based on content")
                                st.markdown("**Sample Question Preview:**")
                                st.info("Q: What concept is discussed in this section from your document?")
                                st.markdown("**Options:** A) Document concept B) Alternative topic C) Different subject D) Other domain")

                            st.success("✅ AI will generate similar questions from your actual PDF content!")

                st.markdown("---")

                col1, col2 = st.columns(2)
                with col1:
                    num_questions = st.selectbox("Number of Questions:", [3, 5, 10], index=1)
                    st.caption("AI will select random sections from your PDFs")
                with col2:
                    difficulty = st.selectbox("Difficulty Level:", ["Easy", "Medium", "Hard"], index=1)
                    st.caption("Affects question complexity and detail level")

                # Enhanced quiz preview with interactive elements
                st.markdown("#### 📋 What to Expect in Your Quiz:")

                # Create interactive preview tabs
                tab1, tab2, tab3 = st.tabs(["📝 Question Format", "🎯 Quiz Experience", "📊 Results & Analysis"])

                with tab1:
                    st.markdown("""
                    **✅ Question Structure:**
                    • **Subject-specific questions** based on your PDF content
                    • **4 multiple-choice options** (A, B, C, D) per question
                    • **1 correct answer** derived from your documents
                    • **Context excerpts** showing the source text from your PDFs
                    • **Source attribution** linking each question to specific documents
                    """)

                    st.markdown("**Example Question Format:**")
                    st.code("""
Q1: What [subject] concept is explained in this section?

📄 Source: Your_Document.pdf
📖 Context: "Excerpt from your PDF content..."

🎯 Choose the correct answer:
○ A) Correct answer based on your content
○ B) Plausible alternative from different subject
○ C) Another reasonable but incorrect option
○ D) Fourth option to complete multiple choice
                    """)

                with tab2:
                    st.markdown("""
                    **✅ Interactive Quiz Features:**
                    • **Animated progress bar** showing completion percentage
                    • **Question navigation** with Previous/Next buttons
                    • **Answer saving** with confirmation feedback
                    • **Source preview** for each question's origin
                    • **Smooth transitions** between questions
                    • **Real-time validation** of answer selections
                    """)

                    st.markdown("**Quiz Flow:**")
                    st.markdown("""
                    1. **Start Quiz** → AI generates questions from your PDFs
                    2. **Answer Questions** → Select from 4 options each
                    3. **Navigate Freely** → Go back/forward as needed
                    4. **Submit Quiz** → Complete when ready
                    5. **View Results** → Detailed analysis and explanations
                    """)

                with tab3:
                    st.markdown("""
                    **✅ Comprehensive Results:**
                    • **Score breakdown** with percentage and grade
                    • **Question-by-question review** with correct answers
                    • **Detailed explanations** for each question
                    • **Performance analysis** with study recommendations
                    • **Source-based feedback** highlighting areas to review
                    • **Downloadable report** for offline study planning
                    """)

                    st.markdown("**Sample Results Preview:**")
                    st.success("🎉 Quiz Completed! Score: 4/5 (80%) - Excellent!")
                    st.info("📋 Detailed review shows correct/incorrect answers with explanations")
                    st.warning("📚 Study recommendations: Focus on [specific topics] from [specific documents]")
                
                # Preview and Start buttons
                col_preview, col_start = st.columns(2)

                with col_preview:
                    if st.button("👀 Preview Questions", type="secondary"):
                        with st.spinner("🤖 Generating preview questions..."):
                            preview_questions = generate_quiz_questions(st.session_state.chunks, 2)
                            if preview_questions:
                                st.markdown("### 🎯 Preview: Questions Generated from Your PDFs")

                                for i, question in enumerate(preview_questions, 1):
                                    st.markdown(f"""
                                    <div style="
                                        background: rgba(255, 255, 255, 0.95);
                                        border: 2px solid rgba(102, 126, 234, 0.3);
                                        border-radius: 15px;
                                        padding: 1.5rem;
                                        margin: 1rem 0;
                                        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
                                    ">
                                        <h4 style="color: #2c3e50;">Preview Question {i}</h4>
                                        <p style="color: #555; font-weight: 500;">{question['question']}</p>
                                        <p style="color: #667eea; font-size: 0.9rem;">📄 Source: {question['source']}</p>
                                        <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                                            <strong>📖 Context:</strong> {question['context'][:150]}...
                                        </div>
                                    </div>
                                    """, unsafe_allow_html=True)

                                    st.markdown("**🎯 Answer Options:**")
                                    for j, option in enumerate(question['options']):
                                        option_letter = chr(65 + j)
                                        if j == question['correct_answer']:
                                            st.success(f"✅ {option_letter}) {option} (Correct Answer)")
                                        else:
                                            st.write(f"○ {option_letter}) {option}")

                                    st.info(f"💡 **Explanation:** {question['explanation']}")
                                    st.markdown("---")

                                st.success("✅ These are the types of questions AI will generate!")

                with col_start:
                    if st.button("🚀 Start Quiz", type="primary"):
                        with st.spinner("🎯 Generating quiz questions from your documents..."):
                            questions = generate_quiz_questions(st.session_state.chunks, num_questions)
                            if questions:
                                st.session_state.quiz_questions = questions
                                st.session_state.quiz_started = True
                                st.session_state.current_question = 0
                                st.session_state.quiz_answers = {}
                                st.session_state.quiz_completed = False
                                st.success(f"✅ Generated {len(questions)} questions from your documents!")
                                st.rerun()
                            else:
                                st.error("❌ Could not generate questions. Please upload more content.")
            
            # Quiz in progress
            elif st.session_state.quiz_started and not st.session_state.quiz_completed:
                questions = st.session_state.quiz_questions
                current_q = st.session_state.current_question
                
                if current_q < len(questions):
                    question = questions[current_q]
                    
                    # Enhanced progress with animations
                    progress = (current_q + 1) / len(questions)

                    # Custom animated progress bar
                    st.markdown(f"""
                    <div style="margin: 1rem 0;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                            <span style="font-weight: 600; color: #2c3e50;">Question {current_q + 1} of {len(questions)}</span>
                            <span style="font-weight: 500; color: #667eea;">{progress:.0%} Complete</span>
                        </div>
                        <div style="
                            width: 100%;
                            height: 12px;
                            background: rgba(102, 126, 234, 0.2);
                            border-radius: 10px;
                            overflow: hidden;
                            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
                        ">
                            <div style="
                                width: {progress * 100}%;
                                height: 100%;
                                background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
                                background-size: 200% 200%;
                                animation: progressShine 2s ease infinite;
                                border-radius: 10px;
                                transition: width 0.5s ease;
                                position: relative;
                            "></div>
                        </div>
                    </div>

                    <style>
                    @keyframes progressShine {{
                        0% {{ background-position: 0% 50%; }}
                        50% {{ background-position: 100% 50%; }}
                        100% {{ background-position: 0% 50%; }}
                    }}
                    </style>
                    """, unsafe_allow_html=True)

                    # Enhanced question display with interactive card
                    st.markdown(f"""
                    <div style="
                        background: rgba(255, 255, 255, 0.95);
                        backdrop-filter: blur(20px);
                        border: 2px solid rgba(102, 126, 234, 0.3);
                        border-radius: 20px;
                        padding: 2rem;
                        margin: 1.5rem 0;
                        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                        animation: questionSlideIn 0.6s ease-out;
                        position: relative;
                        overflow: hidden;
                    ">
                        <div style="
                            position: absolute;
                            top: 0;
                            left: 0;
                            width: 100%;
                            height: 4px;
                            background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
                            background-size: 200% 200%;
                            animation: gradientShift 3s ease infinite;
                        "></div>

                        <h3 style="
                            color: #2c3e50;
                            margin-bottom: 1.5rem;
                            font-weight: 600;
                            font-size: 1.3rem;
                            line-height: 1.4;
                        ">{question['question']}</h3>

                        <div style="
                            display: flex;
                            align-items: center;
                            margin-bottom: 1rem;
                            padding: 0.5rem 1rem;
                            background: rgba(102, 126, 234, 0.1);
                            border-radius: 10px;
                            border-left: 4px solid #667eea;
                        ">
                            <i class="fas fa-file-pdf" style="color: #667eea; margin-right: 0.5rem;"></i>
                            <strong style="color: #2c3e50;">Source Document:</strong>
                            <span style="color: #555; margin-left: 0.5rem;">{question['source']}</span>
                        </div>
                    </div>

                    <style>
                    @keyframes questionSlideIn {{
                        from {{
                            opacity: 0;
                            transform: translateX(-20px);
                        }}
                        to {{
                            opacity: 1;
                            transform: translateX(0);
                        }}
                    }}
                    </style>
                    """, unsafe_allow_html=True)

                    # Enhanced context display
                    st.markdown("**📖 Context from your PDF:**")
                    st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                        border: 2px solid rgba(102, 126, 234, 0.2);
                        border-left: 6px solid #667eea;
                        border-radius: 15px;
                        padding: 1.5rem;
                        margin: 1rem 0;
                        font-style: italic;
                        color: #2c3e50;
                        line-height: 1.6;
                        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
                        animation: contextFadeIn 0.8s ease-out 0.2s both;
                    ">
                        <i class="fas fa-quote-left" style="color: #667eea; margin-right: 0.5rem; opacity: 0.7;"></i>
                        {question['context']}
                        <i class="fas fa-quote-right" style="color: #667eea; margin-left: 0.5rem; opacity: 0.7;"></i>
                    </div>

                    <style>
                    @keyframes contextFadeIn {{
                        from {{
                            opacity: 0;
                            transform: translateY(10px);
                        }}
                        to {{
                            opacity: 1;
                            transform: translateY(0);
                        }}
                    }}
                    </style>
                    """, unsafe_allow_html=True)

                    # Enhanced answer options with interactive styling
                    st.markdown("**🎯 Choose the correct answer (4 options, 1 correct):**")

                    # Create enhanced radio button display
                    st.markdown("""
                    <div style="
                        background: rgba(248, 249, 250, 0.8);
                        border-radius: 15px;
                        padding: 1.5rem;
                        margin: 1rem 0;
                        border: 2px solid rgba(102, 126, 234, 0.2);
                    ">
                        <h4 style="color: #2c3e50; margin-bottom: 1rem; text-align: center;">
                            📝 Select Your Answer Below
                        </h4>
                    </div>
                    """, unsafe_allow_html=True)

                    # Display options with letters A, B, C, D
                    option_letters = ['A', 'B', 'C', 'D']
                    formatted_options = []
                    for i, option in enumerate(question['options']):
                        formatted_options.append(f"{option_letters[i]}) {option}")

                    answer = st.radio(
                        "Select your answer:",
                        formatted_options,
                        key=f"q_{current_q}",
                        index=None,
                        help="💡 Choose the option that best answers the question based on the PDF content above."
                    )

                    # Show selected answer feedback
                    if answer:
                        selected_letter = answer.split(')')[0]
                        selected_text = answer.split(') ', 1)[1] if ') ' in answer else answer

                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
                            border: 2px solid #28a745;
                            border-radius: 12px;
                            padding: 1rem;
                            margin: 1rem 0;
                            animation: selectedAnswer 0.5s ease-out;
                        ">
                            <h4 style="color: #155724; margin: 0;">
                                ✅ Selected Answer: {selected_letter}
                            </h4>
                            <p style="color: #155724; margin: 0.5rem 0 0 0; font-weight: 500;">
                                {selected_text}
                            </p>
                        </div>

                        <style>
                        @keyframes selectedAnswer {{
                            from {{ opacity: 0; transform: translateY(10px); }}
                            to {{ opacity: 1; transform: translateY(0); }}
                        }}
                        </style>
                        """, unsafe_allow_html=True)

                        st.info("💡 You can change your selection before moving to the next question.")

                    # Show generation info
                    with st.expander("ℹ️ How this question was generated"):
                        st.write(f"• **AI Analysis:** This question was automatically generated from your PDF content")
                        st.write(f"• **Source:** Extracted from '{question['source']}'")
                        st.write(f"• **Method:** AI identified key concepts and created multiple-choice options")
                        st.write(f"• **Content Preview:** {question.get('chunk_preview', 'Content analysis...')}")
                    
                    # Enhanced Navigation with better styling
                    st.markdown("---")
                    st.markdown("### 🎮 Quiz Navigation")

                    # Navigation container
                    st.markdown("""
                    <div style="
                        background: rgba(255, 255, 255, 0.9);
                        border-radius: 15px;
                        padding: 1.5rem;
                        margin: 1rem 0;
                        border: 2px solid rgba(102, 126, 234, 0.2);
                        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                    ">
                        <h4 style="text-align: center; color: #2c3e50; margin-bottom: 1rem;">
                            Navigate through your quiz
                        </h4>
                    </div>
                    """, unsafe_allow_html=True)

                    # Check if answer is selected
                    if not answer:
                        st.warning("⚠️ Please select an answer before proceeding!")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        if current_q > 0:
                            if st.button("⬅️ Previous", type="secondary", use_container_width=True):
                                st.session_state.current_question -= 1
                                st.rerun()
                        else:
                            st.info("📍 First Question")

                    with col2:
                        if answer:
                            # Extract actual answer text (remove A), B), etc.)
                            actual_answer = answer.split(') ', 1)[1] if ') ' in answer else answer
                            if st.button("💾 Save Answer", type="primary", use_container_width=True):
                                st.session_state.quiz_answers[current_q] = actual_answer
                                st.success("✅ Answer saved!")
                                st.balloons()
                        else:
                            st.button("💾 Save Answer", disabled=True, use_container_width=True)

                    with col3:
                        if current_q < len(questions) - 1:
                            if st.button("➡️ Next Question", type="primary", use_container_width=True):
                                if answer:
                                    actual_answer = answer.split(') ', 1)[1] if ') ' in answer else answer
                                    st.session_state.quiz_answers[current_q] = actual_answer
                                    st.session_state.current_question += 1
                                    st.success("Moving to next question...")
                                    st.rerun()
                                else:
                                    st.error("Please select an answer first!")
                        else:
                            if st.button("🏁 Finish Quiz", type="primary", use_container_width=True):
                                if answer:
                                    actual_answer = answer.split(') ', 1)[1] if ') ' in answer else answer
                                    st.session_state.quiz_answers[current_q] = actual_answer
                                    st.session_state.quiz_completed = True
                                    st.success("🎉 Quiz completed! Calculating results...")
                                    st.balloons()
                                    st.rerun()
                                else:
                                    st.error("Please select an answer first!")

                    # Show progress summary
                    st.markdown(f"""
                    <div style="
                        text-align: center;
                        margin-top: 1rem;
                        padding: 1rem;
                        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
                        border-radius: 12px;
                        border: 1px solid rgba(102, 126, 234, 0.3);
                    ">
                        <h4 style="color: #2c3e50; margin: 0;">
                            📍 Question {current_q + 1} of {len(questions)}
                        </h4>
                        <p style="color: #555; margin: 0.5rem 0 0 0;">
                            {len(st.session_state.quiz_answers)} answers saved |
                            {len(questions) - len(st.session_state.quiz_answers)} remaining
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Quiz completed
            elif st.session_state.quiz_completed:
                st.markdown("### 🎉 Quiz Completed!")
                
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
                
                # Detailed Question Review with Answers
                st.markdown("---")
                st.markdown("### 📋 Detailed Question Review with Correct Answers")

                for i, question in enumerate(questions):
                    user_answer = answers.get(i, "No answer provided")
                    correct_option = question['options'][question['correct_answer']]
                    is_correct = user_answer == correct_option

                    # Question container
                    with st.container():
                        # Question header with result indicator
                        if is_correct:
                            st.markdown(f"#### ✅ Question {i+1}: CORRECT")
                            st.success("You got this right!")
                        else:
                            st.markdown(f"#### ❌ Question {i+1}: INCORRECT")
                            st.error("Review the correct answer below")

                        # Display the question
                        st.markdown(f"**Question:** {question['question']}")

                        # Show source and context
                        st.markdown(f"**📄 Source:** {question['source']}")
                        with st.expander("📖 View Context from PDF"):
                            st.info(question['context'])

                        # Answer analysis
                        col_a, col_b = st.columns(2)

                        with col_a:
                            st.markdown("**🎯 Your Answer:**")
                            if is_correct:
                                st.success(f"✅ {user_answer}")
                            else:
                                st.error(f"❌ {user_answer}")

                        with col_b:
                            st.markdown("**✅ Correct Answer:**")
                            st.success(f"✅ {correct_option}")

                        # Show all options with indicators
                        st.markdown("**📝 All Answer Options:**")
                        for j, option in enumerate(question['options']):
                            if j == question['correct_answer']:
                                st.markdown(f"✅ **{option}** ← CORRECT ANSWER")
                            elif option == user_answer and not is_correct:
                                st.markdown(f"❌ {option} ← Your choice")
                            else:
                                st.markdown(f"○ {option}")

                        # Explanation
                        st.markdown("**💡 Explanation:**")
                        st.info(question['explanation'])

                        st.markdown("---")

                # Performance Analysis
                st.markdown("### 📊 Performance Analysis")

                if score_percentage >= 80:
                    st.success("🎉 **Excellent Performance!** You have a strong understanding of the material.")
                elif score_percentage >= 60:
                    st.info("👍 **Good Job!** You understand most concepts. Review the incorrect answers to improve.")
                else:
                    st.warning("📚 **Keep Studying!** Review the material and focus on the concepts you missed.")

                # Action buttons
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("🔄 Take New Quiz", type="primary"):
                        st.session_state.quiz_questions = []
                        st.session_state.current_question = 0
                        st.session_state.quiz_answers = {}
                        st.session_state.quiz_started = False
                        st.session_state.quiz_completed = False
                        st.rerun()

                with col2:
                    # Download detailed results
                    results_text = f"StudyMate Quiz Results - Detailed Report\n{'='*60}\n\n"
                    results_text += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    results_text += f"User: {st.session_state.user['name']}\n"
                    results_text += f"Score: {correct_count}/{len(questions)} ({score_percentage:.1f}%)\n\n"

                    for i, question in enumerate(questions):
                        user_answer = answers.get(i, "No answer")
                        correct_option = question['options'][question['correct_answer']]
                        is_correct = user_answer == correct_option

                        results_text += f"Question {i+1}: {'✅ CORRECT' if is_correct else '❌ INCORRECT'}\n"
                        results_text += f"Q: {question['question']}\n"
                        results_text += f"Your Answer: {user_answer}\n"
                        results_text += f"Correct Answer: {correct_option}\n"
                        results_text += f"Source: {question['source']}\n"
                        results_text += f"Explanation: {question['explanation']}\n"
                        results_text += "-" * 50 + "\n\n"

                    st.download_button(
                        label="📥 Download Detailed Results",
                        data=results_text,
                        file_name=f"quiz_results_detailed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )

    with tab3:
        st.markdown("""
        <div class="feature-card">
            <h2>📊 Learning Dashboard</h2>
            <p>Track your learning progress and statistics.</p>
        </div>
        """, unsafe_allow_html=True)

        # Dashboard content
        if st.session_state.chunks:
                "options": [
                    "Calculus and derivatives",
                    "Algebraic equations",
                    "Geometric proofs",
                    "Statistical analysis"
                ],
                "correct_answer": 0,
                "source": "Mathematics_Fundamentals.pdf",
                "context": "Calculus is the mathematical study of continuous change. Derivatives represent the rate of change of a function with respect to a variable, allowing us to analyze how quantities change over time.",
                "explanation": "Calculus, specifically derivatives, is the mathematical tool used to find rates of change. This is fundamental in physics for velocity and acceleration, in economics for marginal analysis, and in engineering for optimization."
            },
            {
                "id": 2,
                "question": "Which programming concept allows code to be reused multiple times?",
                "options": [
                    "Variable declarations",
                    "Functions and methods",
                    "Loop statements",
                    "Conditional logic"
                ],
                "correct_answer": 1,
                "source": "Programming_Fundamentals.pdf",
                "context": "Functions are reusable blocks of code that can be called multiple times with different parameters, promoting code efficiency and maintainability. They encapsulate specific functionality and can return values.",
                "explanation": "Functions and methods allow developers to write code once and reuse it multiple times, which is a fundamental principle of good programming practice called DRY (Don't Repeat Yourself)."
            },
            {
                "id": 3,
