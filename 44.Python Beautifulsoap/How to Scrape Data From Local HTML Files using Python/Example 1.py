# Importing BeautifulSoup and it
# is in the bs4 module
from bs4 import BeautifulSoup

# Opening the html file. If the file
# is present in different location,
# exact location need to be mentioned
HTMLFileToBeOpened = open("samplehtml.html", "r")

# Reading the file and storing in a variable
contents = HTMLFileToBeOpened.read()

# Creating a BeautifulSoup object and
# specifying the parser
beautifulSoupText = BeautifulSoup(contents, 'lxml')

# To get all the tags present in the html
# and getting their length
for tag in beautifulSoupText.findAll(True):
	print(tag.name, " : ", len(beautifulSoupText.find(tag.name).text))
