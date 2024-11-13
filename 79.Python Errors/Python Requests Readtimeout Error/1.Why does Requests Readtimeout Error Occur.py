import requests

try:
	response = requests.get('https://example.com', timeout=5)
	print(response.text)
except requests.exceptions.ReadTimeout:
	print("ReadTimeout error: Server did not respond within the specified timeout.")
