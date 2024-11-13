# 1 - imports
import requests

# 2 - set the siteurl
site_url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'

# 3 - set the headers
headers = {'Accept': 'application/vnd.github.v3+json'}

# 4 - call the url with headers and save the response
response = requests.get(site_url, headers=headers)

# 5 - Get the response
print(f"Response from {site_url} is {response.status_code} ")
