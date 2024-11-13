# import module
from bs4 import BeautifulSoup
import requests

# assign URL
monsterPageURL = 'https://www.geeksforgeeks.org/how-to-scrape-all-pdf-files-in-a-website/'
monsterPage = requests.get(monsterPageURL)

# create Beautiful Soup object
soupResults = BeautifulSoup(monsterPage.content, 'html.parser')

# asign tag
tag="title"

# get length of the tags
print("Length of the text of",tag,"tag is:",
		len(soupResults.find(tag).text))
