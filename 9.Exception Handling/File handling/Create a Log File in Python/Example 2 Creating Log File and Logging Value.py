import logging

# Configure logging with a custom format
logging.basicConfig(filename="gfgnewlog.log", filemode="w", format="%(asctime)s - %(levelname)s - %(message)s")

# Log a warning message
logging.warning("This is a warning")

# Create a logger instance
logger = logging.getLogger(__name__)

# Create a FileHandler to log to 'logs.log' file
file_handler = logging.FileHandler('logs.log')

# Add the FileHandler to the logger
logger.addHandler(file_handler)

# Log a warning message using the logger
logger.warning("This is a test.")
