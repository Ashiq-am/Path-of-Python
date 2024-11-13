# importing the modules
from bs4 import BeautifulSoup
import requests

# URL to the scraped
URL = "https://en.wikipedia.org/wiki/Machine_learning"

# getting the contents of the website and parsing them
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "lxml")

# getting the h1 with id as firstHeading and printing it
title = soup.find("h1", attrs={"id": 'firstHeading'})
print(title)

# getting the text/content inside the h1 tag we
# parsed on the previous line
cont = title.get_text()
print(cont)

# getting the HTML of the parent parent of
# the h1 tag we parsed earlier
parent = soup.find("span",
				attrs={"id": 'Machine_learning_approaches'}).parent()
print(parent)
