# import module
from bs4 import BeautifulSoup
import requests

# Get URL html
# Scarping the data from
# Html doc
url = 'https://www.geeksforgeeks.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Before decomposing
print("Before Decomposing")
print(soup)

# decompose the soup
result = soup.decompose()
print("After decomposing:")
print(result)
