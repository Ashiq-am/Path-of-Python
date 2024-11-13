import requests

try:
	# Simulate a connection error by providing an invalid URL
	response = requests.get("https://example.invalid")
	response.raise_for_status()
except Exception as e:
	# Using a generic except block without specifying the exception type
	print(f"Connection error: {e}")
