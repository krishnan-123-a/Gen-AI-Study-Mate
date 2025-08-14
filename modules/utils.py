"""
Utility Functions for StudyMate
Common helper functions and configurations
"""

import os
import streamlit as st
from typing import Dict, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_environment_variables() -> Dict[str, str]:
    """
    Load environment variables for IBM Watsonx AI
    
    Returns:
        Dictionary with environment variables
    """
    from dotenv import load_dotenv
    
    # Load .env file
    load_dotenv()
    
    env_vars = {
        'IBM_API_KEY': os.getenv('IBM_API_KEY'),
        'IBM_PROJECT_ID': os.getenv('IBM_PROJECT_ID'),
        'IBM_URL': os.getenv('IBM_URL', 'https://us-south.ml.cloud.ibm.com')
    }
    
    return env_vars


def validate_environment() -> bool:
    """
    Validate that all required environment variables are set
    
    Returns:
        True if all variables are set, False otherwise
    """
    env_vars = load_environment_variables()
    
    required_vars = ['IBM_API_KEY', 'IBM_PROJECT_ID', 'IBM_URL']
    missing_vars = []
    
    for var in required_vars:
        if not env_vars.get(var):
            missing_vars.append(var)
    
    if missing_vars:
        logger.error(f"Missing environment variables: {missing_vars}")
        return False
    
    return True


def setup_streamlit_page():
    """Configure Streamlit page settings and styling"""
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .study-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    
    .answer-card {
        background: #f8f9fa;
        border-left: 4px solid #007bff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .source-card {
        background: #e9ecef;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border-left: 3px solid #28a745;
    }
    
    .history-item {
        background: white;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        border: 1px solid #dee2e6;
    }
    
    .upload-section {
        border: 2px dashed #007bff;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        background: #f8f9fa;
    }
    
    .stats-card {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 5px;
        margin: 0.5rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


def display_welcome_message():
    """Display welcome message and instructions"""
    st.markdown("""
    <div class="study-container">
        <h1>📚 StudyMate - Your AI Study Companion</h1>
        <p>Transform your PDFs into an interactive learning experience! Upload your study materials and ask questions to get instant, contextual answers.</p>
        
        <h3>How to use StudyMate:</h3>
        <ol>
            <li><strong>Upload PDFs:</strong> Drag and drop your study materials (lecture notes, textbooks, etc.)</li>
            <li><strong>Ask Questions:</strong> Type natural language questions about your content</li>
            <li><strong>Get Answers:</strong> Receive AI-powered answers with source references</li>
            <li><strong>Review History:</strong> Track your Q&A session and download for later review</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)


def display_processing_stats(stats: Dict):
    """
    Display processing statistics in a nice format
    
    Args:
        stats: Statistics dictionary from PDF processing
    """
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stats-card">
            <h3>{stats.get('total_files', 0)}</h3>
            <p>Total Files</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stats-card">
            <h3>{stats.get('successful_files', 0)}</h3>
            <p>Processed Successfully</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stats-card">
            <h3>{stats.get('total_chunks', 0)}</h3>
            <p>Text Chunks</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stats-card">
            <h3>{stats.get('total_words', 0):,}</h3>
            <p>Total Words</p>
        </div>
        """, unsafe_allow_html=True)


def display_answer_card(qa_response: Dict):
    """
    Display Q&A response in a formatted card
    
    Args:
        qa_response: Q&A response dictionary
    """
    st.markdown(f"""
    <div class="answer-card">
        <h4>💡 Answer:</h4>
        <p>{qa_response['answer']}</p>
        <small><strong>Sources:</strong> {', '.join(qa_response['metadata']['sources'])}</small>
    </div>
    """, unsafe_allow_html=True)


def display_source_chunks(source_chunks: List[Dict]):
    """
    Display source chunks in expandable format
    
    Args:
        source_chunks: List of source chunk dictionaries
    """
    with st.expander("📄 Referenced Paragraphs", expanded=False):
        for i, chunk in enumerate(source_chunks, 1):
            similarity_score = chunk.get('similarity_score', 0)
            st.markdown(f"""
            <div class="source-card">
                <h5>Source {i}: {chunk['source']} (Similarity: {similarity_score:.3f})</h5>
                <p>{chunk['text'][:500]}{'...' if len(chunk['text']) > 500 else ''}</p>
            </div>
            """, unsafe_allow_html=True)


def display_qa_history(qa_history: List[Dict]):
    """
    Display Q&A history in the sidebar
    
    Args:
        qa_history: List of Q&A response dictionaries
    """
    if not qa_history:
        st.sidebar.info("No Q&A history yet. Ask a question to get started!")
        return
    
    st.sidebar.markdown("### 📝 Q&A History")
    
    for i, qa in enumerate(reversed(qa_history), 1):
        with st.sidebar.expander(f"Q{len(qa_history) - i + 1}: {qa['question'][:50]}..."):
            st.write(f"**Q:** {qa['question']}")
            st.write(f"**A:** {qa['answer'][:200]}{'...' if len(qa['answer']) > 200 else ''}")
            st.write(f"**Time:** {qa['timestamp']}")


def create_download_button(qa_history: List[Dict]) -> Optional[str]:
    """
    Create download button for Q&A history
    
    Args:
        qa_history: List of Q&A responses
        
    Returns:
        Download button or None if no history
    """
    if not qa_history:
        return None
    
    # Create export text
    export_text = "StudyMate Q&A Session History\n"
    export_text += "=" * 50 + "\n\n"
    
    for i, qa in enumerate(qa_history, 1):
        export_text += f"Q{i}: {qa['question']}\n"
        export_text += f"A{i}: {qa['answer']}\n"
        export_text += f"Sources: {', '.join(qa['metadata']['sources'])}\n"
        export_text += f"Timestamp: {qa['timestamp']}\n"
        export_text += "-" * 30 + "\n\n"
    
    # Create download button
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"studymate_session_{timestamp}.txt"
    
    st.download_button(
        label="📥 Download Q&A History",
        data=export_text,
        file_name=filename,
        mime="text/plain",
        help="Download your Q&A session for later review"
    )
    
    return export_text


def show_error_message(error: str, details: Optional[str] = None):
    """
    Display error message in a consistent format
    
    Args:
        error: Main error message
        details: Optional detailed error information
    """
    st.error(f"❌ {error}")
    if details:
        with st.expander("Error Details"):
            st.code(details)


def show_success_message(message: str):
    """
    Display success message
    
    Args:
        message: Success message to display
    """
    st.success(f"✅ {message}")


def show_info_message(message: str):
    """
    Display info message
    
    Args:
        message: Info message to display
    """
    st.info(f"ℹ️ {message}")


def initialize_session_state():
    """Initialize Streamlit session state variables"""
    if 'pdf_processor' not in st.session_state:
        st.session_state.pdf_processor = None
    
    if 'embedding_manager' not in st.session_state:
        st.session_state.embedding_manager = None
    
    if 'qa_system' not in st.session_state:
        st.session_state.qa_system = None
    
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = []
    
    if 'qa_history' not in st.session_state:
        st.session_state.qa_history = []
    
    if 'system_ready' not in st.session_state:
        st.session_state.system_ready = False
