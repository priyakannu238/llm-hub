import logging
import os
from datetime import datetime

def setup_logging(log_dir='logs'):
    """
    Configure and setup logging for the application
    
    Args:
        log_dir (str): Directory to store log files
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f'llm_hub_{timestamp}.log')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also output to console
        ]
    )
    
    # Create logger
    logger = logging.getLogger('LLMHub')
    
    # Log system info
    logger.info(f"Logging initialized. Log file: {log_file}")
    
    return logger

class ModelLogger:
    """
    Custom logger for tracking model interactions
    """
    def __init__(self, logger):
        self.logger = logger
    
    def log_model_request(self, model_name, prompt_tokens, system_message):
        """Log details of each model request"""
        self.logger.info(
            f"Model Request: {model_name} | "
            f"System Message Length: {len(system_message)} chars"
        )
    
    def log_model_response(self, model_name, response_length, completion_time):
        """Log details of model response"""
        self.logger.info(
            f"Model Response: {model_name} | "
            f"Response Length: {response_length} chars | "
            f"Completion Time: {completion_time:.2f} seconds"
        )
    
    def log_error(self, error_type, error_message):
        """Log errors encountered during model interaction"""
        self.logger.error(f"Error Type: {error_type} | Message: {error_message}")