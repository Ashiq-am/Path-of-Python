from bs4 import BeautifulSoup
import requests

URL = 'https://www.geeksforgeeks.org/python-update-nested-dictionary/'

# request the page from server
page = requests.get(URL)

# parse the contentes of the page
soup = BeautifulSoup(page.content, "html.parser")

# encoded method
print("Enoded method :", soup.original_encoding)
