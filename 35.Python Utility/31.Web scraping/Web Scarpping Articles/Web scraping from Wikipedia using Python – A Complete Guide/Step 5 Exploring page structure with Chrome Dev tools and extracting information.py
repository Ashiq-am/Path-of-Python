# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
page = requests.get("https://en.wikipedia.org/wiki/Main_Page")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# create object
object = soup.find(id="mp-left")

# find tags
items = object.find_all(class_="mp-h2")
result = items[0]

# display tags
print(result.prettify())
