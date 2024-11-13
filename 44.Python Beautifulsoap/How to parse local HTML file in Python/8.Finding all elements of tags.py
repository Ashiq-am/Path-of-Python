# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("index.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')

# Using the find_all method to find all elements of a tag
for tag in S.find_all('p'):

# Printing the name, and text of p tag
	print(f'{tag.name}: {tag.text}')
