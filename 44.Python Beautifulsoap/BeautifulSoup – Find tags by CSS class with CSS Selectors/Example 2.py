# importing module
from bs4 import BeautifulSoup
import requests

URL = "https://www.geeksforgeeks.org/"
html = requests.get(URL)

# parsering string to HTML
soup = BeautifulSoup(html.content, "html5lib")

# printing tags with given class name
for i in soup.find_all(class_="article--container_content"):
	print(i.name)
