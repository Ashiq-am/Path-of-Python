import sys
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Application started")
        print("Hello, World!")
        logging.info("Application finished successfully")
    except SystemError as e:
        logging.error(f"SystemError: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
