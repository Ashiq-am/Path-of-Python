import requests

try:
	# Simulate a connection error by using an invalid protocol
	response = requests.get("ftp://example.com")
	response.raise_for_status()
except requests.exceptions.RequestException as e:
	# The exception message may not provide sufficient information
	print(f"Connection error: {e}")
