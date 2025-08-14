"""
PDF Processing Module for StudyMate
Handles PDF text extraction and intelligent chunking with overlap
"""

import fitz  # PyMuPDF
import re
from typing import List, Dict, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFProcessor:
    """Handles PDF text extraction and chunking operations"""
    
    def __init__(self, chunk_size: int = 500, overlap_size: int = 100):
        """
        Initialize PDF processor with chunking parameters
        
        Args:
            chunk_size: Target number of words per chunk
            overlap_size: Number of words to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size
    
    def extract_text_from_pdf(self, pdf_file) -> str:
        """
        Extract text from uploaded PDF file
        
        Args:
            pdf_file: Streamlit uploaded file object
            
        Returns:
            Extracted text as string
        """
        try:
            # Read PDF from uploaded file
            pdf_bytes = pdf_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document.page(page_num)
                text += page.get_text()
            
            pdf_document.close()
            
            # Clean up the text
            text = self._clean_text(text)
            
            logger.info(f"Successfully extracted {len(text)} characters from {pdf_file.name}")
            return text
            
        except Exception as e:
            logger.error(f"Error extracting text from {pdf_file.name}: {str(e)}")
            raise Exception(f"Failed to process PDF {pdf_file.name}: {str(e)}")
    
    def _clean_text(self, text: str) -> str:
        """
        Clean extracted text by removing extra whitespace and formatting issues
        
        Args:
            text: Raw extracted text
            
        Returns:
            Cleaned text
        """
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove page numbers and headers/footers (basic patterns)
        text = re.sub(r'\n\d+\n', '\n', text)
        
        # Remove special characters that might interfere with processing
        text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\[\]\{\}\"\'\/]', '', text)
        
        return text.strip()
    
    def chunk_text(self, text: str, source_filename: str) -> List[Dict[str, str]]:
        """
        Split text into overlapping chunks for better semantic retrieval
        
        Args:
            text: Text to chunk
            source_filename: Name of source file for reference
            
        Returns:
            List of dictionaries containing chunk text, metadata, and source info
        """
        words = text.split()
        chunks = []
        
        if len(words) <= self.chunk_size:
            # If text is smaller than chunk size, return as single chunk
            chunks.append({
                'text': text,
                'source': source_filename,
                'chunk_id': 0,
                'word_count': len(words)
            })
            return chunks
        
        start_idx = 0
        chunk_id = 0
        
        while start_idx < len(words):
            # Calculate end index for current chunk
            end_idx = min(start_idx + self.chunk_size, len(words))
            
            # Extract chunk words
            chunk_words = words[start_idx:end_idx]
            chunk_text = ' '.join(chunk_words)
            
            # Create chunk metadata
            chunk_data = {
                'text': chunk_text,
                'source': source_filename,
                'chunk_id': chunk_id,
                'word_count': len(chunk_words),
                'start_word': start_idx,
                'end_word': end_idx
            }
            
            chunks.append(chunk_data)
            
            # Move start index forward, accounting for overlap
            start_idx = end_idx - self.overlap_size
            chunk_id += 1
            
            # Break if we've reached the end
            if end_idx >= len(words):
                break
        
        logger.info(f"Created {len(chunks)} chunks from {source_filename}")
        return chunks
    
    def process_multiple_pdfs(self, pdf_files: List) -> Tuple[List[Dict[str, str]], Dict[str, int]]:
        """
        Process multiple PDF files and return all chunks with statistics
        
        Args:
            pdf_files: List of Streamlit uploaded file objects
            
        Returns:
            Tuple of (all_chunks, processing_stats)
        """
        all_chunks = []
        stats = {
            'total_files': len(pdf_files),
            'successful_files': 0,
            'failed_files': 0,
            'total_chunks': 0,
            'total_words': 0
        }
        
        for pdf_file in pdf_files:
            try:
                # Extract text from PDF
                text = self.extract_text_from_pdf(pdf_file)
                
                # Create chunks
                chunks = self.chunk_text(text, pdf_file.name)
                all_chunks.extend(chunks)
                
                # Update statistics
                stats['successful_files'] += 1
                stats['total_chunks'] += len(chunks)
                stats['total_words'] += len(text.split())
                
            except Exception as e:
                logger.error(f"Failed to process {pdf_file.name}: {str(e)}")
                stats['failed_files'] += 1
                continue
        
        logger.info(f"Processing complete: {stats['successful_files']}/{stats['total_files']} files successful")
        return all_chunks, stats
    
    def get_chunk_preview(self, chunk: Dict[str, str], max_length: int = 200) -> str:
        """
        Get a preview of chunk content for display purposes
        
        Args:
            chunk: Chunk dictionary
            max_length: Maximum length of preview text
            
        Returns:
            Preview text with ellipsis if truncated
        """
        text = chunk['text']
        if len(text) <= max_length:
            return text
        
        # Find a good breaking point near the max length
        truncated = text[:max_length]
        last_space = truncated.rfind(' ')
        
        if last_space > max_length * 0.8:  # If we found a space reasonably close to the end
            return truncated[:last_space] + "..."
        else:
            return truncated + "..."


def create_pdf_processor(chunk_size: int = 500, overlap_size: int = 100) -> PDFProcessor:
    """
    Factory function to create a PDF processor instance
    
    Args:
        chunk_size: Target words per chunk
        overlap_size: Overlap words between chunks
        
    Returns:
        Configured PDFProcessor instance
    """
    return PDFProcessor(chunk_size=chunk_size, overlap_size=overlap_size)
