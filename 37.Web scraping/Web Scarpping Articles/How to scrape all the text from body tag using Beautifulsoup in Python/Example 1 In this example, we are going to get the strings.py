# Import Beautiful Soup
from bs4 import BeautifulSoup

# Create the document
doc = "<body><b> Hello world </b><h1> New heading </h1><body>"

# Initialize the object with the document
soup = BeautifulSoup(doc, "html.parser")

# Get the whole body tag
tag = soup.body

# Print each string recursivey
for string in tag.strings:
	print(string)
