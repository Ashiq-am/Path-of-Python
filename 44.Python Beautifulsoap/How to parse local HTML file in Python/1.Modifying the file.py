# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Importing the HTTP library
import requests as req

# Requesting for the website
Web = req.get('https://festive-knuth-1279a2.netlify.app/')

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(Web.text, 'lxml')

# Using the prettify method
print(S.prettify())
