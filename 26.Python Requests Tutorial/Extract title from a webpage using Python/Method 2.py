# importing the modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

# target url
url = 'https://www.geeksforgeeks.org/'

# using the BeaitifulSoup module
soup = BeautifulSoup(urlopen(url))

# displaying the title
print("Title of the website is : ")
print (soup.title.get_text())
