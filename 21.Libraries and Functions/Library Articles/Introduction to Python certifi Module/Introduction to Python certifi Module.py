# Import the necessary modules
import requests
import certifi

# Make a secure GET request to a website
response = requests.get("https://www.geeksforgeeks.org/", verify=certifi.where())

# Check if the request was successful
if response.status_code == 200:
    print("The website is secure and reachable!")
else:
    print("Failed to reach the website.")
