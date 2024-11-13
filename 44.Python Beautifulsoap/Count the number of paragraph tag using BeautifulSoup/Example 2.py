# Python program to get number of paragraph tags
# of a given Website in Beautifulsoup

# Import the libraries beautifulsoup
# and os
from bs4 import BeautifulSoup as bs
import os
import requests

# Assign URL
URL = 'https://www.geeksforgeeks.org/'

# Page content from Website URL
page = requests.get(URL)

# Parse HTML file in Beautiful Soup
soup = bs(page.content, 'html.parser')

# Print a certain line
print("Number of paragraph tags:")

# Calculating and printing the
# number of paragraph tags
print(len(soup.find_all("p")))
