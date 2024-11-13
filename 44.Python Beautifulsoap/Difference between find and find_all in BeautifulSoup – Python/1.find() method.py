# Find example

# Import the libraries BeautifulSoup
# and os
from bs4 import BeautifulSoup as bs
import os

# Remove the last segment of the path
base=os.path.dirname(os.path.abspath(__file__))

# Open the HTML in which you want to
# make changes
html=open(os.path.join(base, 'gfg.html'))

# Parse HTML file in Beautiful Soup
soup=bs(html, 'html.parser')

# Obtain the text from the widget after
# finding it
find_example=soup.find("p", {"id":"vinayak"}).get_text()

# Printing the text obtained received
# in previous step
print(find_example)
