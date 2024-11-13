# importing the modules
from bs4 import BeautifulSoup
import requests

# URL to the scraped
URL = "https://en.wikipedia.org/wiki/Machine_learning"

# getting the contents of the website and parsing them
webpage = requests.get(URL)
soup = BeautifulSoup(webpage.content, "lxml")
