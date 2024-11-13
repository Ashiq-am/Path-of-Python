# Import request module
import requests

# store the response from an API in response
response = requests.get("https://api.github.com")

# Checking if the reponse status
if response.status_code == 200:
	print("Successfully connected to GitHub API!")
else:
	print("Failed to connect to GitHub API!")
