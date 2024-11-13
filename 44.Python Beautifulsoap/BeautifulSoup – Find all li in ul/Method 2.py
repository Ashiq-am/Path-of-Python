# importing the modules
import requests
from bs4 import BeautifulSoup

# providing url
url = 'https://auth.geeksforgeeks.org/user/adityaprasad1308/articles'

# creating request object
req = requests.get(url)

# creating soup object
data = BeautifulSoup(req.text, 'html')

# finding all li tags in ul and printing the text within it
data1 = data.find('ul')
for li in data1.find_all("li"):
	print(li.text, end=" ")
