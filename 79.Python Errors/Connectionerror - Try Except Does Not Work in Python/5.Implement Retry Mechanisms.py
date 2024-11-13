import requests
from requests.exceptions import RequestException
from retrying import retry # Install using: pip install retrying

@retry(wait_exponential_multiplier=1000, stop_max_attempt_number=5)
def make_request():
	# Your code that may raise a connection error
	response = requests.get("https://example.com")
	response.raise_for_status()

try:
	make_request()
except RequestException as e:
	print(f"Connection error: {e}")
