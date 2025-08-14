"""
Test Script for StudyMate Application
Tests individual components and integration
"""

import os
import sys
import logging
from typing import List, Dict
import tempfile

# Add modules to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.pdf_processor import create_pdf_processor
from modules.embeddings import create_embedding_manager
from modules.llm_integration import create_watsonx_llm, create_qa_system
from modules.utils import load_environment_variables, validate_environment

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_environment():
    """Test environment configuration"""
    print("🔧 Testing Environment Configuration...")
    
    try:
        env_vars = load_environment_variables()
        is_valid = validate_environment()
        
        print(f"Environment validation: {'✅ PASS' if is_valid else '❌ FAIL'}")
        
        if not is_valid:
            print("Please ensure your .env file contains:")
            print("- IBM_API_KEY")
            print("- IBM_PROJECT_ID") 
            print("- IBM_URL")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Environment test failed: {str(e)}")
        return False


def test_pdf_processor():
    """Test PDF processing functionality"""
    print("\n📄 Testing PDF Processor...")
    
    try:
        # Create processor
        processor = create_pdf_processor()
        
        # Test text chunking with sample text
        sample_text = "This is a test document. " * 100  # Create longer text
        chunks = processor.chunk_text(sample_text, "test.pdf")
        
        print(f"✅ Created {len(chunks)} chunks from sample text")
        print(f"✅ First chunk has {chunks[0]['word_count']} words")
        
        return True
        
    except Exception as e:
        print(f"❌ PDF processor test failed: {str(e)}")
        return False


def test_embedding_manager():
    """Test embedding and vector search functionality"""
    print("\n🔍 Testing Embedding Manager...")
    
    try:
        # Create embedding manager
        embedding_manager = create_embedding_manager()
        
        # Test with sample chunks
        sample_chunks = [
            {"text": "Machine learning is a subset of artificial intelligence.", "source": "test1.pdf", "chunk_id": 0},
            {"text": "Deep learning uses neural networks with multiple layers.", "source": "test1.pdf", "chunk_id": 1},
            {"text": "Natural language processing helps computers understand text.", "source": "test2.pdf", "chunk_id": 0}
        ]
        
        # Create embeddings
        embeddings = embedding_manager.create_embeddings(sample_chunks)
        print(f"✅ Created embeddings with shape: {embeddings.shape}")
        
        # Build FAISS index
        index = embedding_manager.build_faiss_index()
        print(f"✅ Built FAISS index with {index.ntotal} vectors")
        
        # Test search
        results = embedding_manager.search_similar_chunks("What is machine learning?", k=2)
        print(f"✅ Search returned {len(results)} results")
        
        return True
        
    except Exception as e:
        print(f"❌ Embedding manager test failed: {str(e)}")
        return False


def test_llm_integration():
    """Test IBM Watsonx LLM integration"""
    print("\n🤖 Testing LLM Integration...")
    
    try:
        # Load environment variables
        env_vars = load_environment_variables()
        
        # Create LLM
        llm = create_watsonx_llm(
            api_key=env_vars['IBM_API_KEY'],
            project_id=env_vars['IBM_PROJECT_ID'],
            url=env_vars['IBM_URL']
        )
        
        # Test connection
        connection_ok = llm.test_connection()
        print(f"Connection test: {'✅ PASS' if connection_ok else '❌ FAIL'}")
        
        if connection_ok:
            # Test answer generation
            sample_context = "Machine learning is a method of data analysis that automates analytical model building."
            sample_query = "What is machine learning?"
            sample_chunks = [{"text": sample_context, "source": "test.pdf"}]
            
            answer, metadata = llm.generate_answer(sample_query, sample_context, sample_chunks)
            print(f"✅ Generated answer: {answer[:100]}...")
            print(f"✅ Metadata: {metadata['model_used']}")
        
        return connection_ok
        
    except Exception as e:
        print(f"❌ LLM integration test failed: {str(e)}")
        return False


def test_qa_system():
    """Test complete Q&A system"""
    print("\n💬 Testing Q&A System...")
    
    try:
        # Load environment variables
        env_vars = load_environment_variables()
        
        # Create components
        llm = create_watsonx_llm(
            api_key=env_vars['IBM_API_KEY'],
            project_id=env_vars['IBM_PROJECT_ID'],
            url=env_vars['IBM_URL']
        )
        
        qa_system = create_qa_system(llm)
        
        # Test Q&A
        sample_context = "Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans."
        sample_query = "What is artificial intelligence?"
        sample_chunks = [{"text": sample_context, "source": "ai_textbook.pdf"}]
        
        qa_response = qa_system.answer_question(sample_query, sample_context, sample_chunks)
        
        print(f"✅ Q&A response generated")
        print(f"✅ Question: {qa_response['question']}")
        print(f"✅ Answer: {qa_response['answer'][:100]}...")
        
        # Test history
        history = qa_system.get_qa_history()
        print(f"✅ History contains {len(history)} items")
        
        # Test export
        export_text = qa_system.export_history_text()
        print(f"✅ Export text length: {len(export_text)} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Q&A system test failed: {str(e)}")
        return False


def run_all_tests():
    """Run all tests and provide summary"""
    print("🧪 StudyMate Component Testing")
    print("=" * 50)
    
    tests = [
        ("Environment", test_environment),
        ("PDF Processor", test_pdf_processor),
        ("Embedding Manager", test_embedding_manager),
        ("LLM Integration", test_llm_integration),
        ("Q&A System", test_qa_system)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} test crashed: {str(e)}")
            results[test_name] = False
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! StudyMate is ready to use.")
    else:
        print("⚠️ Some tests failed. Please check the configuration and try again.")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
