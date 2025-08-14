"""
StudyMate Demo Script
Demonstrates the core functionality without Streamlit interface
"""

import os
import sys
from typing import List, Dict

# Add modules to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.pdf_processor import create_pdf_processor
from modules.embeddings import create_embedding_manager
from modules.llm_integration import create_watsonx_llm, create_qa_system
from modules.utils import load_environment_variables, validate_environment


def create_sample_content():
    """Create sample academic content for demonstration"""
    sample_documents = [
        {
            "filename": "machine_learning_basics.pdf",
            "content": """
            Machine Learning Fundamentals
            
            Machine learning is a subset of artificial intelligence (AI) that provides systems 
            the ability to automatically learn and improve from experience without being explicitly 
            programmed. Machine learning focuses on the development of computer programs that can 
            access data and use it to learn for themselves.
            
            Types of Machine Learning:
            
            1. Supervised Learning: Uses labeled training data to learn a mapping function from 
            input variables to output variables. Examples include classification and regression.
            
            2. Unsupervised Learning: Finds hidden patterns in data without labeled examples. 
            Common techniques include clustering and dimensionality reduction.
            
            3. Reinforcement Learning: An agent learns to make decisions by taking actions in 
            an environment to maximize cumulative reward.
            
            Key Algorithms:
            - Linear Regression: Predicts continuous values
            - Decision Trees: Creates a model that predicts target values
            - Neural Networks: Mimics the human brain structure
            - Support Vector Machines: Finds optimal decision boundaries
            """
        },
        {
            "filename": "deep_learning_concepts.pdf", 
            "content": """
            Deep Learning and Neural Networks
            
            Deep learning is a subset of machine learning that uses artificial neural networks 
            with multiple layers (hence "deep") to model and understand complex patterns in data.
            
            Neural Network Architecture:
            
            1. Input Layer: Receives the raw data
            2. Hidden Layers: Process the data through weighted connections
            3. Output Layer: Produces the final prediction or classification
            
            Key Concepts:
            
            Activation Functions: Mathematical functions that determine the output of a neural 
            network node. Common types include ReLU, Sigmoid, and Tanh.
            
            Backpropagation: The algorithm used to train neural networks by calculating 
            gradients and updating weights to minimize error.
            
            Convolutional Neural Networks (CNNs): Specialized for processing grid-like data 
            such as images. Uses convolutional layers to detect features.
            
            Recurrent Neural Networks (RNNs): Designed for sequential data like text or time 
            series. Can maintain memory of previous inputs.
            
            Applications:
            - Image recognition and computer vision
            - Natural language processing
            - Speech recognition
            - Autonomous vehicles
            """
        }
    ]
    
    return sample_documents


def demo_pdf_processing():
    """Demonstrate PDF processing functionality"""
    print("📄 Demo: PDF Processing")
    print("-" * 40)
    
    # Create sample content
    documents = create_sample_content()
    
    # Initialize PDF processor
    processor = create_pdf_processor(chunk_size=200, overlap_size=50)
    
    all_chunks = []
    for doc in documents:
        print(f"Processing: {doc['filename']}")
        chunks = processor.chunk_text(doc['content'], doc['filename'])
        all_chunks.extend(chunks)
        print(f"  Created {len(chunks)} chunks")
    
    print(f"\nTotal chunks created: {len(all_chunks)}")
    print(f"Sample chunk preview: {all_chunks[0]['text'][:100]}...")
    
    return all_chunks


def demo_embeddings(chunks: List[Dict]):
    """Demonstrate embedding and search functionality"""
    print("\n🔍 Demo: Semantic Search")
    print("-" * 40)
    
    # Initialize embedding manager
    embedding_manager = create_embedding_manager()
    
    # Create embeddings
    print("Creating embeddings...")
    embeddings = embedding_manager.create_embeddings(chunks)
    print(f"Embeddings shape: {embeddings.shape}")
    
    # Build FAISS index
    print("Building search index...")
    index = embedding_manager.build_faiss_index()
    print(f"Index contains {index.ntotal} vectors")
    
    # Test search queries
    test_queries = [
        "What is machine learning?",
        "Explain neural networks",
        "What are the types of machine learning?",
        "How does backpropagation work?"
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        results = embedding_manager.search_similar_chunks(query, k=2)
        
        for i, (chunk, score) in enumerate(results, 1):
            print(f"  Result {i} (score: {score:.3f}): {chunk['text'][:80]}...")
    
    return embedding_manager


def demo_qa_system(embedding_manager):
    """Demonstrate complete Q&A system"""
    print("\n💬 Demo: Q&A System")
    print("-" * 40)
    
    # Check environment
    if not validate_environment():
        print("❌ Environment not configured. Skipping LLM demo.")
        print("Please set up your .env file with IBM Watsonx credentials.")
        return
    
    try:
        # Initialize LLM
        env_vars = load_environment_variables()
        llm = create_watsonx_llm(
            api_key=env_vars['IBM_API_KEY'],
            project_id=env_vars['IBM_PROJECT_ID'],
            url=env_vars['IBM_URL']
        )
        
        # Test connection
        print("Testing LLM connection...")
        if not llm.test_connection():
            print("❌ LLM connection failed")
            return
        
        print("✅ LLM connection successful")
        
        # Create Q&A system
        qa_system = create_qa_system(llm)
        
        # Demo questions
        demo_questions = [
            "What is the difference between supervised and unsupervised learning?",
            "Explain what deep learning is and how it relates to neural networks"
        ]
        
        for question in demo_questions:
            print(f"\n🤔 Question: {question}")
            
            # Get context
            context, source_chunks = embedding_manager.get_context_for_query(question, k=2)
            
            if context:
                # Generate answer
                qa_response = qa_system.answer_question(question, context, source_chunks)
                
                print(f"🤖 Answer: {qa_response['answer']}")
                print(f"📚 Sources: {', '.join(qa_response['metadata']['sources'])}")
            else:
                print("❌ No relevant context found")
        
        # Show history
        history = qa_system.get_qa_history()
        print(f"\n📝 Q&A History: {len(history)} interactions")
        
        # Export demo
        export_text = qa_system.export_history_text()
        print(f"📄 Export length: {len(export_text)} characters")
        
    except Exception as e:
        print(f"❌ Q&A demo failed: {str(e)}")


def main():
    """Run the complete demo"""
    print("🎯 StudyMate Functionality Demo")
    print("=" * 50)
    
    # Demo PDF processing
    chunks = demo_pdf_processing()
    
    # Demo embeddings and search
    embedding_manager = demo_embeddings(chunks)
    
    # Demo Q&A system
    demo_qa_system(embedding_manager)
    
    print("\n🎉 Demo completed!")
    print("\nTo try the full Streamlit interface, run:")
    print("streamlit run app.py")


if __name__ == "__main__":
    main()
