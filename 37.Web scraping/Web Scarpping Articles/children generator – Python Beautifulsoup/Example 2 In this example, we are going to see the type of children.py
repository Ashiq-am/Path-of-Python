# Import Beautiful Soup
from bs4 import BeautifulSoup

# Create the document
doc = "<body><b> Hello world </b><body>"

# Initialize the object with the document
soup = BeautifulSoup(doc, "html.parser")

# Get the body tag
tag = soup.body

# Print the type of children of tag
for child in tag.children:
	print(type(child))
