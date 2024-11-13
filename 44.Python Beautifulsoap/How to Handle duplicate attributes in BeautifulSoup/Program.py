# Import the libraries beautifulsoup and os
from bs4 import BeautifulSoup as bs
import os

# Remove the last segment of the path
# Here replace the name of your python file with
# gfg4.py
base = os.path.dirname(os.path.abspath("gfg4.py"))

# Open the HTML in which you want to make
# changes
html = open(os.path.join(base, 'gfg.html'))

# Parse HTML file in Beautiful Soup
soup = bs(html, 'html.parser')

# Create a list to store the items
list = [3]

# Finding all the elements inside div
# with paragraph having id: vinayak
list = soup.div.find_all("p", {"id": "vinayak"})

# Removing attributes from the output
for i in list:
	i.attrs = {}

# Printing the value Prince
print(list[1])

# Printing the value Queen
print(list[2])
