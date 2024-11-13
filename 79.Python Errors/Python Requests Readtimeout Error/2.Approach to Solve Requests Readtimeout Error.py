import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def fetch_data_with_retry(url, timeout=5, retries=3):
	"""
	Fetches data from a URL with retry mechanism in case of ReadTimeout error.
	"""
	session = requests.Session()
	retry_strategy = Retry(
		total=retries,
		backoff_factor=0.5,
		status_forcelist=[500, 502, 503, 504],
	)
	adapter = HTTPAdapter(max_retries=retry_strategy)
	session.mount("http://", adapter)
	session.mount("https://", adapter)

	try:
		response = session.get(url, timeout=timeout)
		response.raise_for_status()
		return response.text
	except requests.exceptions.ReadTimeout:
		print("ReadTimeout error: Server did not respond within the specified timeout.")
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
	return None

# Example usage:
url = 'https://example.com'
data = fetch_data_with_retry(url)
if data:
	print("Data fetched successfully:", data)
else:
	print("Failed to fetch data.")
