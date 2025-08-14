"""
IBM Watsonx LLM Integration Module for StudyMate
Handles AI-powered answer generation using IBM Watsonx AI
"""

import os
from typing import Dict, List, Optional, Tuple
import logging
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WatsonxLLM:
    """Handles IBM Watsonx AI integration for answer generation"""
    
    def __init__(self, api_key: str, project_id: str, url: str):
        """
        Initialize Watsonx LLM with credentials
        
        Args:
            api_key: IBM Cloud API key
            project_id: IBM Watsonx project ID
            url: IBM Watsonx service URL
        """
        self.api_key = api_key
        self.project_id = project_id
        self.url = url
        self.model = None
        self.is_initialized = False
        
        # Model configuration
        self.model_id = "mistralai/mixtral-8x7b-instruct-v01"
        self.generation_params = {
            GenParams.DECODING_METHOD: "greedy",
            GenParams.TEMPERATURE: 0.3,
            GenParams.MAX_NEW_TOKENS: 300,
            GenParams.MIN_NEW_TOKENS: 10,
            GenParams.STOP_SEQUENCES: ["</s>", "\n\nHuman:", "\n\nUser:"]
        }
    
    def initialize_model(self):
        """Initialize the Watsonx model with credentials"""
        try:
            logger.info("Initializing IBM Watsonx AI model...")
            
            # Set up credentials
            credentials = Credentials(
                url=self.url,
                api_key=self.api_key
            )
            
            # Initialize model
            self.model = Model(
                model_id=self.model_id,
                params=self.generation_params,
                credentials=credentials,
                project_id=self.project_id
            )
            
            self.is_initialized = True
            logger.info(f"Successfully initialized {self.model_id}")
            
        except Exception as e:
            logger.error(f"Failed to initialize Watsonx model: {str(e)}")
            raise Exception(f"Failed to initialize IBM Watsonx AI: {str(e)}")
    
    def create_prompt(self, query: str, context: str, source_info: List[Dict]) -> str:
        """
        Create a well-structured prompt for the LLM
        
        Args:
            query: User's question
            context: Retrieved context from documents
            source_info: Information about source documents
            
        Returns:
            Formatted prompt string
        """
        # Get unique source files
        sources = list(set(chunk['source'] for chunk in source_info))
        source_list = ", ".join(sources)
        
        prompt = f"""You are StudyMate, an AI study assistant helping students understand their academic materials. 

Based on the provided context from the student's uploaded documents, answer the following question accurately and helpfully.

**Context from documents ({source_list}):**
{context}

**Student's Question:**
{query}

**Instructions:**
- Provide a clear, accurate answer based on the context provided
- If the context doesn't contain enough information, say so honestly
- Use simple, student-friendly language
- Include specific details from the context when relevant
- Keep your response focused and concise (under 300 words)

**Answer:**"""
        
        return prompt
    
    def generate_answer(self, query: str, context: str, source_chunks: List[Dict]) -> Tuple[str, Dict]:
        """
        Generate an answer using the Watsonx LLM
        
        Args:
            query: User's question
            context: Retrieved context text
            source_chunks: List of source chunk dictionaries
            
        Returns:
            Tuple of (generated_answer, metadata)
        """
        if not self.is_initialized:
            self.initialize_model()
        
        try:
            # Create prompt
            prompt = self.create_prompt(query, context, source_chunks)
            
            logger.info("Generating answer with Watsonx AI...")
            
            # Generate response
            response = self.model.generate_text(prompt=prompt)
            
            # Extract the answer
            answer = response.strip()
            
            # Create metadata
            metadata = {
                'model_used': self.model_id,
                'context_length': len(context),
                'num_source_chunks': len(source_chunks),
                'sources': list(set(chunk['source'] for chunk in source_chunks)),
                'generation_params': self.generation_params
            }
            
            logger.info("Successfully generated answer")
            return answer, metadata
            
        except Exception as e:
            logger.error(f"Error generating answer: {str(e)}")
            raise Exception(f"Failed to generate answer: {str(e)}")
    
    def test_connection(self) -> bool:
        """
        Test the connection to IBM Watsonx AI
        
        Returns:
            True if connection successful, False otherwise
        """
        try:
            if not self.is_initialized:
                self.initialize_model()
            
            # Test with a simple prompt
            test_prompt = "Hello, this is a connection test. Please respond with 'Connection successful.'"
            response = self.model.generate_text(prompt=test_prompt)
            
            logger.info("Connection test successful")
            return True
            
        except Exception as e:
            logger.error(f"Connection test failed: {str(e)}")
            return False
    
    def update_generation_params(self, **kwargs):
        """
        Update generation parameters
        
        Args:
            **kwargs: Parameter updates (temperature, max_tokens, etc.)
        """
        for key, value in kwargs.items():
            if hasattr(GenParams, key.upper()):
                param_name = getattr(GenParams, key.upper())
                self.generation_params[param_name] = value
                logger.info(f"Updated {key} to {value}")
        
        # Reinitialize model with new parameters if already initialized
        if self.is_initialized:
            self.model.set_params(self.generation_params)


class StudyMateQA:
    """High-level Q&A system combining retrieval and generation"""
    
    def __init__(self, llm: WatsonxLLM):
        """
        Initialize Q&A system
        
        Args:
            llm: Initialized WatsonxLLM instance
        """
        self.llm = llm
        self.qa_history = []
    
    def answer_question(self, query: str, context: str, source_chunks: List[Dict]) -> Dict:
        """
        Generate a complete Q&A response
        
        Args:
            query: User's question
            context: Retrieved context
            source_chunks: Source chunk information
            
        Returns:
            Complete Q&A response dictionary
        """
        try:
            # Generate answer
            answer, metadata = self.llm.generate_answer(query, context, source_chunks)
            
            # Create complete response
            qa_response = {
                'question': query,
                'answer': answer,
                'source_chunks': source_chunks,
                'metadata': metadata,
                'timestamp': self._get_timestamp()
            }
            
            # Add to history
            self.qa_history.append(qa_response)
            
            return qa_response
            
        except Exception as e:
            logger.error(f"Error in Q&A process: {str(e)}")
            raise
    
    def get_qa_history(self) -> List[Dict]:
        """Get the complete Q&A history"""
        return self.qa_history
    
    def clear_history(self):
        """Clear the Q&A history"""
        self.qa_history = []
        logger.info("Q&A history cleared")
    
    def export_history_text(self) -> str:
        """
        Export Q&A history as formatted text
        
        Returns:
            Formatted text string of all Q&A interactions
        """
        if not self.qa_history:
            return "No Q&A history available."
        
        export_text = "StudyMate Q&A Session History\n"
        export_text += "=" * 50 + "\n\n"
        
        for i, qa in enumerate(self.qa_history, 1):
            export_text += f"Q{i}: {qa['question']}\n"
            export_text += f"A{i}: {qa['answer']}\n"
            
            # Add source information
            sources = qa['metadata']['sources']
            export_text += f"Sources: {', '.join(sources)}\n"
            export_text += f"Timestamp: {qa['timestamp']}\n"
            export_text += "-" * 30 + "\n\n"
        
        return export_text
    
    def _get_timestamp(self) -> str:
        """Get current timestamp as string"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_watsonx_llm(api_key: str, project_id: str, url: str) -> WatsonxLLM:
    """
    Factory function to create a WatsonxLLM instance
    
    Args:
        api_key: IBM Cloud API key
        project_id: IBM Watsonx project ID
        url: IBM Watsonx service URL
        
    Returns:
        Configured WatsonxLLM instance
    """
    return WatsonxLLM(api_key=api_key, project_id=project_id, url=url)


def create_qa_system(llm: WatsonxLLM) -> StudyMateQA:
    """
    Factory function to create a StudyMateQA instance
    
    Args:
        llm: Initialized WatsonxLLM instance
        
    Returns:
        Configured StudyMateQA instance
    """
    return StudyMateQA(llm=llm)
