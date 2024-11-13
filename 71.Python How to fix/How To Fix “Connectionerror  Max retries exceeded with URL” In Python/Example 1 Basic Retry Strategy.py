import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session
session = requests.Session()

# Define a retry strategy
retry_strategy = Retry(
    total=5,  # Total number of retries
    backoff_factor=1,  # Waits 1 second between retries, then 2s, 4s, 8s...
    status_forcelist=[429, 500, 502, 503, 504],  # Status codes to retry on
    method_whitelist=["HEAD", "GET", "OPTIONS"]  # Methods to retry
)

# Mount the retry strategy to the session
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("http://", adapter)
session.mount("https://", adapter)

# Make a request
try:
    response = session.get("https://example.com")
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(response.content)  # Handle the response
except requests.exceptions.ConnectionError as e:
    print(f"Error connecting to the server: {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# This code is contributed by Susobhan Akhuli
