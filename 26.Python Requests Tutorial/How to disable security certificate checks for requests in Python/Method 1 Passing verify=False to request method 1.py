import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# sending a get http request to specified url
response = requests.get("https://www.geeksforgeeks.org/",
						verify=False)

# response data
print(response)
