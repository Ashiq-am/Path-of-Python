import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a session
session = requests.Session()

# Define a retry strategy
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)

# Mount the retry strategy to the session
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Make a request
url = "https://example.com"
try:
    response = session.get(url)
    response.raise_for_status()
    logger.info("Request successful.")
    logger.info(f"Response: {response.content}")
except requests.exceptions.ConnectionError as e:
    logger.error(f"Connection error: {e}")
except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    logger.error(f"General error: {e}")

# This code is contributed by Susobhan Akhuli
