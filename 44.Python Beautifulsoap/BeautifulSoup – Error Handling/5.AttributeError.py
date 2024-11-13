# importing modules
import requests
import bs4

url = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'

# geting response from server
response = requests.get(url)

# extracting html
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# for printing attribute error
print(soup.NoneExistingTag.SomeTag)
