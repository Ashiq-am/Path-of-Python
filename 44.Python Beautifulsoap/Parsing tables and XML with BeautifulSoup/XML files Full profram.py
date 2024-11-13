# import required modules
from bs4 import BeautifulSoup

# reading content
file = open("test1.xml", "r")
contents = file.read()

# parsing
soup = BeautifulSoup(contents, 'xml')
titles = soup.find_all('title')

# display content
for data in titles:
	print(data.get_text())
