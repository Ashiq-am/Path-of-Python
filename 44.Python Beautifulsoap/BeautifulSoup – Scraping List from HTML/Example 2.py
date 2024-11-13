# Import Required Moduels
from bs4 import BeautifulSoup
import requests

# Web URL
url = "https://www.geeksforgeeks.org/python-list/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Find all li tag
datas = soup.find_all("li")

# Iterate through all li tags
for data in datas:
	# Get text from each tag
	print(data.text)

print(f"Total {len(datas)} li tag found")
