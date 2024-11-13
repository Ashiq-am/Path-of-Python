# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# display scrapped data
print(soup.prettify())
