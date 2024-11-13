import requests

def fetch_data():
	# Making an API request that fails
	response = requests.get("https://example.com/api/data")
	if response.status_code != 200:
		return None

	return response.json()

# Attempting to unpack values from the API response
data = fetch_data()
try:
	a, b = data # Raises "Cannot Unpack Non-iterable NoneType Objects" error
except TypeError as e:
	print(f"Error: {e}")
