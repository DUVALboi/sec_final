import logging
import os

def setup_logging(log_file='logs/security_automation.log'):
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
