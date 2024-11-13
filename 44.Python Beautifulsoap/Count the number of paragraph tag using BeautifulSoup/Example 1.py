# Python program to get number of paragraph tags
# of a given HTML document in Beautifulsoup

# Import the libraries beautifulsoup
# and os
from bs4 import BeautifulSoup as bs
import os

# Open the HTML file
html = open('gfg.html')

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Print a certain line
print("Number of paragraph tags:")

# Calculating and printing the
# number of paragraph tags
print(len(soup.find_all("p")))
