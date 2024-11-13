# Import modules
from bs4 import BeautifulSoup
import requests

# Assign URL
url = "https://www.geeksforgeeks.org/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content using any parser
soup = BeautifulSoup(html_content, "html.parser")

# Display HTML tags
[tag.name for tag in soup.find_all()]
