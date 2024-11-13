# Import Required Module
import requests
from bs4 import BeautifulSoup

# Web URL
Web_url = "https://www.geeksforgeeks.org/"

# Get URL Content
r = requests.get(Web_url)

# Parse HTML Code
soup = BeautifulSoup(r.content, 'html.parser')

tag = soup.find("p")

print(tag.get_text())
