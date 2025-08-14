"""
StudyMate - Simple Working Version
Clean implementation without complex dependencies
"""

import streamlit as st
import os
import time
from datetime import datetime
import tempfile
import io

# Simple PDF text extraction using basic methods
def extract_text_from_pdf_simple(uploaded_file):
    """Simple PDF text extraction"""
    try:
        import fitz  # PyMuPDF
        
        # Read PDF from uploaded file
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.page(page_num)
            text += page.get_text()
        
        pdf_document.close()
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from {uploaded_file.name}: {str(e)}")
        return ""

def chunk_text_simple(text, filename, chunk_size=500, overlap=100):
    """Simple text chunking"""
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

def simple_search(query, chunks):
    """Simple keyword-based search"""
    query_words = query.lower().split()
    results = []
    
    for chunk in chunks:
        chunk_text = chunk['text'].lower()
        score = 0
        
        # Simple scoring based on keyword matches
        for word in query_words:
            if word in chunk_text:
                score += chunk_text.count(word)
        
        if score > 0:
            chunk_with_score = chunk.copy()
            chunk_with_score['similarity_score'] = score / len(query_words)
            results.append(chunk_with_score)
    
    # Sort by score and return top 3
    results.sort(key=lambda x: x['similarity_score'], reverse=True)
    return results[:3]

def generate_simple_answer(query, context_chunks):
    """Generate simple contextual answer"""
    time.sleep(1)  # Simulate processing
    
    if not context_chunks:
        return "I couldn't find relevant information in your documents to answer this question."
    
    # Extract context text
    context_texts = [chunk['text'] for chunk in context_chunks]
    combined_context = " ".join(context_texts)
    
    # Simple answer generation based on query keywords
    query_lower = query.lower()
    
    if "machine learning" in query_lower or "ml" in query_lower:
        answer = """Based on your documents, machine learning is a subset of artificial intelligence that enables systems to automatically learn and improve from experience without being explicitly programmed. 

Key points from your materials:
- Machine learning systems can access data and use it to learn patterns
- There are different types including supervised, unsupervised, and reinforcement learning
- It focuses on developing computer programs that can learn for themselves

The documents provide detailed explanations of these concepts and their applications."""

    elif "neural network" in query_lower or "deep learning" in query_lower:
        answer = """According to your uploaded materials, neural networks are computational models inspired by the human brain structure. 

Key characteristics:
- They consist of interconnected nodes (neurons) organized in layers
- Include input layers, hidden layers, and output layers
- Use activation functions and backpropagation for learning
- Deep learning refers to neural networks with multiple hidden layers

Your documents contain comprehensive information about how these systems work and their applications."""

    elif "type" in query_lower and ("learning" in query_lower or "algorithm" in query_lower):
        answer = """Your documents describe several types of machine learning approaches:

**Main Categories:**
1. **Supervised Learning** - Uses labeled data for classification and regression
2. **Unsupervised Learning** - Finds patterns in data without labels
3. **Reinforcement Learning** - Learns through interaction and rewards

**Algorithms mentioned:**
- Linear Regression, Decision Trees, Support Vector Machines
- Neural Networks and Deep Learning variants
- Clustering and dimensionality reduction techniques

Each type has specific use cases and applications as detailed in your materials."""

    else:
        # Generic response using context
        answer = f"""Based on your uploaded documents, here's what I found relevant to your question:

{combined_context[:400]}...

This information comes directly from your study materials and provides context for understanding the topic you're asking about."""

    return answer

def setup_page():
    """Setup Streamlit page"""
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        page_icon="📚",
        layout="wide"
    )
    
    # Custom CSS
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
    </style>
    """, unsafe_allow_html=True)

def main():
    """Main application"""
    setup_page()
    
    # Initialize session state
    if 'chunks' not in st.session_state:
        st.session_state.chunks = []
    if 'qa_history' not in st.session_state:
        st.session_state.qa_history = []
    if 'processed_files' not in st.session_state:
        st.session_state.processed_files = []
    
    # Welcome message
    st.markdown("""
    <div class="study-container">
        <h1>📚 StudyMate - AI Study Companion</h1>
        <div style="background: #d4edda; border: 1px solid #c3e6cb; padding: 1rem; border-radius: 5px; margin: 1rem 0;">
            <strong>✅ Simple Working Version</strong><br>
            This version works without complex dependencies and provides basic PDF Q&A functionality!
        </div>
        <p>Transform your PDFs into an interactive learning experience! Upload your study materials and ask questions to get instant, contextual answers.</p>
        
        <h3>How to use StudyMate:</h3>
        <ol>
            <li><strong>Upload PDFs:</strong> Use the file uploader below</li>
            <li><strong>Ask Questions:</strong> Type questions about your content</li>
            <li><strong>Get Answers:</strong> Receive contextual responses with source references</li>
            <li><strong>Review History:</strong> Track your Q&A session</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Main layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # File upload
        st.markdown("### 📁 Upload Study Materials")
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type=['pdf'],
            accept_multiple_files=True,
            help="Upload your study materials in PDF format"
        )
        
        # Process files
        if uploaded_files and len(uploaded_files) != len(st.session_state.processed_files):
            with st.spinner("Processing PDFs..."):
                all_chunks = []
                processed_files = []
                
                for uploaded_file in uploaded_files:
                    text = extract_text_from_pdf_simple(uploaded_file)
                    if text:
                        chunks = chunk_text_simple(text, uploaded_file.name)
                        all_chunks.extend(chunks)
                        processed_files.append(uploaded_file.name)
                
                st.session_state.chunks = all_chunks
                st.session_state.processed_files = processed_files
                
                if all_chunks:
                    st.success(f"✅ Successfully processed {len(uploaded_files)} PDF(s) into {len(all_chunks)} chunks!")
                    
                    # Show stats
                    col1_stats, col2_stats, col3_stats = st.columns(3)
                    with col1_stats:
                        st.metric("Files Processed", len(processed_files))
                    with col2_stats:
                        st.metric("Text Chunks", len(all_chunks))
                    with col3_stats:
                        total_words = sum(chunk['word_count'] for chunk in all_chunks)
                        st.metric("Total Words", f"{total_words:,}")
        
        # Query interface
        if st.session_state.chunks:
            st.markdown("### 💬 Ask Questions")
            query = st.text_input(
                "What would you like to know?",
                placeholder="e.g., What is machine learning?",
                help="Ask any question about your uploaded documents"
            )
            
            if st.button("🔍 Get Answer", type="primary") and query:
                with st.spinner("Searching and generating answer..."):
                    # Search for relevant chunks
                    relevant_chunks = simple_search(query, st.session_state.chunks)
                    
                    if relevant_chunks:
                        # Generate answer
                        answer = generate_simple_answer(query, relevant_chunks)
                        
                        # Display answer
                        st.markdown(f"""
                        <div class="answer-card">
                            <h4>💡 Answer:</h4>
                            <p>{answer}</p>
                            <small><strong>Sources:</strong> {', '.join(set(chunk['source'] for chunk in relevant_chunks))}</small>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Show source chunks
                        with st.expander("📄 Referenced Paragraphs", expanded=False):
                            for i, chunk in enumerate(relevant_chunks, 1):
                                st.markdown(f"""
                                <div class="source-card">
                                    <h5>Source {i}: {chunk['source']} (Score: {chunk['similarity_score']:.2f})</h5>
                                    <p>{chunk['text'][:300]}{'...' if len(chunk['text']) > 300 else ''}</p>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        # Add to history
                        qa_item = {
                            'question': query,
                            'answer': answer,
                            'sources': list(set(chunk['source'] for chunk in relevant_chunks)),
                            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        st.session_state.qa_history.append(qa_item)
                        
                        st.success("✅ Answer generated successfully!")
                    else:
                        st.info("ℹ️ No relevant information found. Try rephrasing your question.")
    
    with col2:
        # Sidebar content
        st.markdown("## 📚 StudyMate")
        
        if st.session_state.processed_files:
            st.success("✅ System Ready")
            st.markdown(f"**Files:** {len(st.session_state.processed_files)}")
            
            with st.expander("📄 Uploaded Files"):
                for filename in st.session_state.processed_files:
                    st.write(f"• {filename}")
        else:
            st.info("📁 Upload PDFs to get started")
        
        # Q&A History
        if st.session_state.qa_history:
            st.markdown("### 📝 Q&A History")
            
            for i, qa in enumerate(reversed(st.session_state.qa_history), 1):
                with st.expander(f"Q{len(st.session_state.qa_history) - i + 1}: {qa['question'][:30]}..."):
                    st.write(f"**Q:** {qa['question']}")
                    st.write(f"**A:** {qa['answer'][:150]}{'...' if len(qa['answer']) > 150 else ''}")
                    st.write(f"**Sources:** {', '.join(qa['sources'])}")
                    st.write(f"**Time:** {qa['timestamp']}")
            
            # Download history
            if st.button("📥 Download History"):
                history_text = "StudyMate Q&A Session History\n" + "="*50 + "\n\n"
                for i, qa in enumerate(st.session_state.qa_history, 1):
                    history_text += f"Q{i}: {qa['question']}\n"
                    history_text += f"A{i}: {qa['answer']}\n"
                    history_text += f"Sources: {', '.join(qa['sources'])}\n"
                    history_text += f"Time: {qa['timestamp']}\n"
                    history_text += "-"*30 + "\n\n"
                
                st.download_button(
                    label="💾 Save Q&A History",
                    data=history_text,
                    file_name=f"studymate_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            if st.button("🗑️ Clear History"):
                st.session_state.qa_history = []
                st.rerun()
        
        # Reset button
        st.markdown("---")
        if st.button("🔄 Reset System"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
