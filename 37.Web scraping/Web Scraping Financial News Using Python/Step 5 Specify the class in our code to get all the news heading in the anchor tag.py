# IMPORT ALL LIBRARIES
from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.businesstoday.in/latest/economy"

webpage = req.get(url) # YOU CAN EVEN DIRECTLY PASTE THE URL IN THIS
# HERE HTML PARSER IS ACTUALLY THE WHOLE HTML PAGE
trav = BS(webpage.content, "html.parser")

# TO GET THE TPYE OF CLASS
# HERE 'a' STANDS FOR ANCHOR TAG IN WHICH NEWS IS STORED
for link in trav.find_all('a'):
	print(type(link.string), " ", link.string)
