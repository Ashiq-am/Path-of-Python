# Import Module
from bs4 import BeautifulSoup
import requests

# Assing website
import requests
URL = "https://www.geeksforgeeks.org/"
HTML_DOC = requests.get(URL)

# Function to find tags
def find_tags_from_class(html):

	# parse html content
	soup = BeautifulSoup(html.content, "html5lib")

	# find tags by CSS class
	div = soup.find("div", class_= "article--container_content")

	# Print the extracted tag
	print(div)

# Function Call
find_tags_from_class(HTML_DOC)
