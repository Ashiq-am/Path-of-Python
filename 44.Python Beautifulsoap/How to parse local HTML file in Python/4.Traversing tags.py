# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("index.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')

# Using the recursiveChildGenerator method to traverse the html file
for TraverseTags in S.recursiveChildGenerator():
# Traversing the names of the tags
	if TraverseTags.name:
	# Printing the names of the tags
		print(TraverseTags.name)
