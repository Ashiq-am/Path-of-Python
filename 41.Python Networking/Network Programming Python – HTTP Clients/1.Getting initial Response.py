# Import libraries
import requests

# Sending Request
req = requests.get('https://www.geeksforgeeks.org/')

# Show results
print(req.text[:2000])
