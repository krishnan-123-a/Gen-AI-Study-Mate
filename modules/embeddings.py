"""
Embeddings and Vector Database Module for StudyMate
Handles semantic embeddings creation and FAISS similarity search
"""

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Tuple, Optional
import logging
import pickle

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Manages semantic embeddings and vector similarity search"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize embedding manager with SentenceTransformer model
        
        Args:
            model_name: Name of the SentenceTransformer model to use
        """
        self.model_name = model_name
        self.model = None
        self.index = None
        self.chunks = []
        self.embeddings = None
        self.is_initialized = False
        
    def initialize_model(self):
        """Initialize the SentenceTransformer model"""
        try:
            logger.info(f"Loading SentenceTransformer model: {self.model_name}")
            self.model = SentenceTransformer(self.model_name)
            self.is_initialized = True
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise Exception(f"Failed to initialize embedding model: {str(e)}")
    
    def create_embeddings(self, chunks: List[Dict[str, str]]) -> np.ndarray:
        """
        Create embeddings for text chunks
        
        Args:
            chunks: List of chunk dictionaries containing text and metadata
            
        Returns:
            Numpy array of embeddings
        """
        if not self.is_initialized:
            self.initialize_model()
        
        try:
            # Extract text from chunks
            texts = [chunk['text'] for chunk in chunks]
            
            logger.info(f"Creating embeddings for {len(texts)} chunks...")
            
            # Generate embeddings
            embeddings = self.model.encode(
                texts,
                convert_to_numpy=True,
                show_progress_bar=True,
                batch_size=32
            )
            
            # Store chunks and embeddings
            self.chunks = chunks
            self.embeddings = embeddings
            
            logger.info(f"Successfully created embeddings with shape: {embeddings.shape}")
            return embeddings
            
        except Exception as e:
            logger.error(f"Error creating embeddings: {str(e)}")
            raise Exception(f"Failed to create embeddings: {str(e)}")
    
    def build_faiss_index(self, embeddings: Optional[np.ndarray] = None) -> faiss.Index:
        """
        Build FAISS index for fast similarity search
        
        Args:
            embeddings: Optional embeddings array (uses stored if not provided)
            
        Returns:
            FAISS index
        """
        if embeddings is None:
            embeddings = self.embeddings
            
        if embeddings is None:
            raise ValueError("No embeddings available. Create embeddings first.")
        
        try:
            # Get embedding dimension
            dimension = embeddings.shape[1]
            
            logger.info(f"Building FAISS index with dimension: {dimension}")
            
            # Create FAISS index (using IndexFlatIP for cosine similarity)
            index = faiss.IndexFlatIP(dimension)
            
            # Normalize embeddings for cosine similarity
            faiss.normalize_L2(embeddings)
            
            # Add embeddings to index
            index.add(embeddings.astype('float32'))
            
            self.index = index
            
            logger.info(f"FAISS index built successfully with {index.ntotal} vectors")
            return index
            
        except Exception as e:
            logger.error(f"Error building FAISS index: {str(e)}")
            raise Exception(f"Failed to build FAISS index: {str(e)}")
    
    def search_similar_chunks(self, query: str, k: int = 3) -> List[Tuple[Dict[str, str], float]]:
        """
        Search for most similar chunks to a query
        
        Args:
            query: Search query text
            k: Number of top results to return
            
        Returns:
            List of tuples (chunk_dict, similarity_score)
        """
        if not self.is_initialized:
            raise ValueError("Model not initialized. Call initialize_model() first.")
        
        if self.index is None:
            raise ValueError("FAISS index not built. Call build_faiss_index() first.")
        
        try:
            # Create embedding for query
            query_embedding = self.model.encode([query], convert_to_numpy=True)
            
            # Normalize query embedding
            faiss.normalize_L2(query_embedding)
            
            # Search in FAISS index
            similarities, indices = self.index.search(query_embedding.astype('float32'), k)
            
            # Prepare results
            results = []
            for i, (similarity, idx) in enumerate(zip(similarities[0], indices[0])):
                if idx < len(self.chunks):  # Ensure valid index
                    chunk = self.chunks[idx]
                    results.append((chunk, float(similarity)))
            
            logger.info(f"Found {len(results)} similar chunks for query")
            return results
            
        except Exception as e:
            logger.error(f"Error searching similar chunks: {str(e)}")
            raise Exception(f"Failed to search similar chunks: {str(e)}")
    
    def get_context_for_query(self, query: str, k: int = 3) -> Tuple[str, List[Dict[str, str]]]:
        """
        Get contextual information for a query by retrieving similar chunks
        
        Args:
            query: User query
            k: Number of chunks to retrieve
            
        Returns:
            Tuple of (combined_context_text, list_of_source_chunks)
        """
        similar_chunks = self.search_similar_chunks(query, k)
        
        if not similar_chunks:
            return "", []
        
        # Extract context text and source information
        context_texts = []
        source_chunks = []
        
        for chunk, similarity in similar_chunks:
            context_texts.append(chunk['text'])
            
            # Add similarity score to chunk info for reference
            chunk_with_score = chunk.copy()
            chunk_with_score['similarity_score'] = similarity
            source_chunks.append(chunk_with_score)
        
        # Combine context texts
        combined_context = "\n\n".join(context_texts)
        
        return combined_context, source_chunks
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Get statistics about the current embedding database
        
        Returns:
            Dictionary with statistics
        """
        stats = {
            'model_name': self.model_name,
            'is_initialized': self.is_initialized,
            'total_chunks': len(self.chunks),
            'embedding_dimension': self.embeddings.shape[1] if self.embeddings is not None else 0,
            'index_size': self.index.ntotal if self.index is not None else 0,
            'unique_sources': len(set(chunk['source'] for chunk in self.chunks)) if self.chunks else 0
        }
        
        return stats
    
    def clear_database(self):
        """Clear all stored embeddings and index"""
        self.chunks = []
        self.embeddings = None
        self.index = None
        logger.info("Embedding database cleared")


def create_embedding_manager(model_name: str = "all-MiniLM-L6-v2") -> EmbeddingManager:
    """
    Factory function to create an embedding manager instance
    
    Args:
        model_name: SentenceTransformer model name
        
    Returns:
        Configured EmbeddingManager instance
    """
    return EmbeddingManager(model_name=model_name)
