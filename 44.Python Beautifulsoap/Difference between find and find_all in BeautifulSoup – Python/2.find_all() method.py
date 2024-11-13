# find_all example

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

# Construct a loop to find all the
# p tags
for word in soup.find_all('p'):

	# Obtain the text from the received
	# tags
	find_all_example=word.get_text()

	# Print the text obtained received
	# in previous step
	print(find_all_example)
