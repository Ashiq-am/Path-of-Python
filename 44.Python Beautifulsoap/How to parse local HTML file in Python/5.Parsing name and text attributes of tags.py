# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("index.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')

# Printing the Code, name, and text of a tag
print(f'HTML: {S.ul}, name: {S.ul.name}, text: {S.ul.text}')
