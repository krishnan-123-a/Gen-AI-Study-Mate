"""
StudyMate Demo Application - Works without IBM Watsonx credentials
Demonstrates full functionality with mock LLM responses
"""

import streamlit as st
import os
from typing import List, Dict
import logging
import time
from datetime import datetime

# Import custom modules
from modules.pdf_processor import create_pdf_processor
from modules.embeddings import create_embedding_manager
from modules.utils import (
    setup_streamlit_page, display_welcome_message,
    display_processing_stats, display_answer_card,
    display_source_chunks, display_qa_history, create_download_button,
    show_error_message, show_success_message, show_info_message,
    initialize_session_state
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MockLLM:
    """Mock LLM for demonstration purposes"""
    
    def generate_answer(self, query: str, context: str, source_chunks: List[Dict]) -> tuple:
        """Generate a mock answer based on the query and context"""
        
        # Simulate processing time
        time.sleep(1)
        
        # Generate contextual answer based on query keywords
        if "machine learning" in query.lower():
            answer = """Machine learning is a subset of artificial intelligence that enables systems to automatically learn and improve from experience without being explicitly programmed. Based on your documents, there are three main types:

1. **Supervised Learning**: Uses labeled data to learn mappings from inputs to outputs
2. **Unsupervised Learning**: Finds hidden patterns in data without labels  
3. **Reinforcement Learning**: Learns through interaction with an environment

The key is that ML systems can access data and use it to learn patterns and make predictions on new, unseen data."""

        elif "neural network" in query.lower() or "deep learning" in query.lower():
            answer = """Neural networks are computational models inspired by the human brain structure. They consist of interconnected nodes (neurons) organized in layers:

- **Input Layer**: Receives raw data
- **Hidden Layers**: Process data through weighted connections (this is where "deep" learning gets its name - multiple hidden layers)
- **Output Layer**: Produces final predictions

Key concepts include activation functions (like ReLU, Sigmoid) that determine neuron outputs, and backpropagation - the algorithm used to train networks by calculating gradients and updating weights to minimize error."""

        elif "type" in query.lower() and "learning" in query.lower():
            answer = """According to your uploaded materials, there are several types of machine learning approaches:

**Main Categories:**
1. **Supervised Learning** - Classification and regression with labeled examples
2. **Unsupervised Learning** - Clustering and dimensionality reduction  
3. **Reinforcement Learning** - Learning through rewards and actions

**Deep Learning Subcategories:**
- **CNNs (Convolutional Neural Networks)** - Specialized for image processing
- **RNNs (Recurrent Neural Networks)** - Designed for sequential data like text

Each type is suited for different kinds of problems and data structures."""

        elif "algorithm" in query.lower():
            answer = """Your documents mention several key machine learning algorithms:

**Traditional ML Algorithms:**
- **Linear Regression**: Predicts continuous values using linear relationships
- **Decision Trees**: Creates tree-like models for classification and regression
- **Support Vector Machines**: Finds optimal decision boundaries between classes

**Deep Learning Algorithms:**
- **Backpropagation**: Core training algorithm for neural networks
- **Gradient Descent**: Optimization method for minimizing loss functions

Each algorithm has specific strengths and is chosen based on the problem type, data size, and interpretability requirements."""

        else:
            # Generic response based on context
            answer = f"""Based on your uploaded documents, here's what I found relevant to your question:

{context[:300]}...

This information comes from your study materials and provides context for understanding the concepts you're asking about. The documents contain detailed explanations that can help deepen your understanding of this topic."""

        metadata = {
            'model_used': 'StudyMate Demo LLM',
            'context_length': len(context),
            'num_source_chunks': len(source_chunks),
            'sources': list(set(chunk['source'] for chunk in source_chunks)),
            'generation_params': {'mode': 'demo', 'response_time': '1s'}
        }
        
        return answer, metadata


class MockQASystem:
    """Mock Q&A system for demonstration"""
    
    def __init__(self):
        self.llm = MockLLM()
        self.qa_history = []
    
    def answer_question(self, query: str, context: str, source_chunks: List[Dict]) -> Dict:
        """Generate a complete Q&A response"""
        answer, metadata = self.llm.generate_answer(query, context, source_chunks)
        
        qa_response = {
            'question': query,
            'answer': answer,
            'source_chunks': source_chunks,
            'metadata': metadata,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.qa_history.append(qa_response)
        return qa_response
    
    def get_qa_history(self) -> List[Dict]:
        return self.qa_history
    
    def clear_history(self):
        self.qa_history = []


def main():
    """Main application function"""
    # Setup page configuration
    setup_streamlit_page()
    
    # Initialize session state
    initialize_session_state()
    
    # Display welcome message with demo notice
    st.markdown("""
    <div class="study-container">
        <h1>📚 StudyMate - AI Study Companion (Demo Mode)</h1>
        <div style="background: #fff3cd; border: 1px solid #ffeaa7; padding: 1rem; border-radius: 5px; margin: 1rem 0;">
            <strong>🎯 Demo Mode Active:</strong> This version works without IBM Watsonx credentials and uses mock AI responses for demonstration. 
            The PDF processing, embeddings, and search functionality are fully functional!
        </div>
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
    
    # Main application layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # PDF Upload Section
        st.markdown("### 📁 Upload Study Materials")
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type=['pdf'],
            accept_multiple_files=True,
            help="Upload your lecture notes, textbooks, or any study materials in PDF format"
        )
        
        # Process uploaded files
        if uploaded_files and not st.session_state.system_ready:
            process_uploaded_files(uploaded_files)
        
        # Query Section
        if st.session_state.system_ready:
            st.markdown("### 💬 Ask Questions")
            query_interface()
    
    with col2:
        # Sidebar content
        sidebar_content()


def process_uploaded_files(uploaded_files: List):
    """Process uploaded PDF files and prepare the system"""
    try:
        with st.spinner("Processing your PDFs..."):
            # Initialize PDF processor
            if st.session_state.pdf_processor is None:
                st.session_state.pdf_processor = create_pdf_processor()
            
            # Process PDFs
            chunks, stats = st.session_state.pdf_processor.process_multiple_pdfs(uploaded_files)
            
            if not chunks:
                show_error_message("No content extracted from PDFs. Please check your files.")
                return
            
            # Display processing statistics
            st.markdown("### 📊 Processing Results")
            display_processing_stats(stats)
            
            # Initialize embedding manager
            if st.session_state.embedding_manager is None:
                st.session_state.embedding_manager = create_embedding_manager()
            
            # Create embeddings
            with st.spinner("Creating semantic embeddings..."):
                embeddings = st.session_state.embedding_manager.create_embeddings(chunks)
                st.session_state.embedding_manager.build_faiss_index(embeddings)
            
            # Initialize Mock Q&A system
            if st.session_state.qa_system is None:
                st.session_state.qa_system = MockQASystem()
            
            # Mark system as ready
            st.session_state.system_ready = True
            st.session_state.processed_files = [f.name for f in uploaded_files]
            
            show_success_message(f"Successfully processed {len(uploaded_files)} PDF(s). You can now ask questions!")
            
    except Exception as e:
        logger.error(f"Error processing files: {str(e)}")
        show_error_message("Processing Error", str(e))


def query_interface():
    """Handle user queries and display answers"""
    # Query input
    query = st.text_input(
        "What would you like to know?",
        placeholder="e.g., What are the main concepts in machine learning?",
        help="Ask any question about your uploaded documents"
    )
    
    # Process query
    if st.button("🔍 Get Answer", type="primary") and query:
        try:
            with st.spinner("Searching for relevant information..."):
                # Get context from embeddings
                context, source_chunks = st.session_state.embedding_manager.get_context_for_query(query, k=3)
                
                if not context:
                    show_info_message("No relevant information found for your query. Try rephrasing your question.")
                    return
                
                # Generate answer
                with st.spinner("Generating answer..."):
                    qa_response = st.session_state.qa_system.answer_question(query, context, source_chunks)
                
                # Display answer
                display_answer_card(qa_response)
                
                # Display source chunks
                display_source_chunks(source_chunks)
                
                # Update session state
                st.session_state.qa_history = st.session_state.qa_system.get_qa_history()
                
                show_success_message("Answer generated successfully!")
                
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            show_error_message("Query Processing Error", str(e))


def sidebar_content():
    """Display sidebar content"""
    st.sidebar.markdown("## 📚 StudyMate Demo")
    
    # Demo mode notice
    st.sidebar.info("🎯 Running in Demo Mode\nMock AI responses active")
    
    # System status
    if st.session_state.system_ready:
        st.sidebar.success("✅ System Ready")
        st.sidebar.markdown(f"**Processed Files:** {len(st.session_state.processed_files)}")
        
        # Display processed files
        if st.session_state.processed_files:
            with st.sidebar.expander("📄 Uploaded Files"):
                for filename in st.session_state.processed_files:
                    st.write(f"• {filename}")
    else:
        st.sidebar.info("📁 Upload PDFs to get started")
    
    # Q&A History
    if st.session_state.qa_history:
        display_qa_history(st.session_state.qa_history)
        
        # Download button
        st.sidebar.markdown("---")
        create_download_button(st.session_state.qa_history)
        
        # Clear history button
        if st.sidebar.button("🗑️ Clear History"):
            st.session_state.qa_history = []
            if st.session_state.qa_system:
                st.session_state.qa_system.clear_history()
            st.rerun()
    
    # System information
    st.sidebar.markdown("---")
    with st.sidebar.expander("ℹ️ System Info"):
        if st.session_state.embedding_manager:
            stats = st.session_state.embedding_manager.get_statistics()
            st.write(f"**Model:** {stats['model_name']}")
            st.write(f"**Chunks:** {stats['total_chunks']}")
            st.write(f"**Sources:** {stats['unique_sources']}")
        else:
            st.write("System not initialized")
    
    # Reset system button
    st.sidebar.markdown("---")
    if st.sidebar.button("🔄 Reset System"):
        reset_system()


def reset_system():
    """Reset the entire system"""
    try:
        # Clear session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        
        # Reinitialize
        initialize_session_state()
        
        show_success_message("System reset successfully!")
        st.rerun()
        
    except Exception as e:
        logger.error(f"Error resetting system: {str(e)}")
        show_error_message("Reset Error", str(e))


if __name__ == "__main__":
    main()
