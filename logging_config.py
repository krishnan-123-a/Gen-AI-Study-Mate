"""
Logging Configuration for StudyMate
Centralized logging setup for all modules
"""

import logging
import os
from datetime import datetime


def setup_logging(log_level=logging.INFO, log_to_file=True):
    """
    Setup logging configuration for StudyMate
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_to_file: Whether to log to file in addition to console
    """
    
    # Create logs directory if it doesn't exist
    if log_to_file:
        os.makedirs("logs", exist_ok=True)
    
    # Configure logging format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    
    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt=date_format,
        force=True
    )
    
    # Add file handler if requested
    if log_to_file:
        # Create log filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d")
        log_filename = f"logs/studymate_{timestamp}.log"
        
        # Create file handler
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(log_format, date_format))
        
        # Add to root logger
        logging.getLogger().addHandler(file_handler)
    
    # Set specific logger levels
    logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
    logging.getLogger("transformers").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    
    logging.info("Logging configured successfully")


def get_logger(name):
    """
    Get a logger instance for a specific module
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)


# Initialize logging when module is imported
setup_logging()
