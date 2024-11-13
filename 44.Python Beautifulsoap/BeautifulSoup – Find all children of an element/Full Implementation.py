# Python program to find all the children
# of an element using Beautiful Soup

# Import the libraries BeautifulSoup and os
from bs4 import BeautifulSoup as bs
import os

# Remove the last segment of the path
# Give same name in abspath as given to Python file
base = os.path.dirname(os.path.abspath('run.py'))

# Open the HTML in which you want to make changes
html = open(os.path.join(base, 'gfg.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Give location where text is stored which you wish to alter
unordered_list = soup.find("ul", {"id": "list"})

# Find children of an element
children = unordered_list.findChildren()

# Print all children of an element
for child in children:
	print(child)
