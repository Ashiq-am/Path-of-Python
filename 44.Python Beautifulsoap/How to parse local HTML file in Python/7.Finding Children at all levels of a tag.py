# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("index.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')

# Providing the source
Des = S.body

# Using the descendants attribute
Attr_Tag = [e.name for e in Des.descendants if e.name is not None]

# Printing the children
print(Attr_Tag)
