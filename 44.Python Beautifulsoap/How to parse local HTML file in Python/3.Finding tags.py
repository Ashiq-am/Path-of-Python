# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("index.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
Parse = BeautifulSoup(index, 'lxml')

# Printing html code of some tags
print(Parse.head)
print(Parse.h1)
print(Parse.h2)
print(Parse.h3)
print(Parse.li)
