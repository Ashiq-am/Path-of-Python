# code
import requests

# The following line makes an https request, and stores the response
# in the variable 'r'
r = requests.get("https://www.google.com")

# The following line give us the response code
r.status_code
