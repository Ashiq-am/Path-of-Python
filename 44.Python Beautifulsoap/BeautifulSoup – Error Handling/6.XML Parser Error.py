import requests
import bs4

url = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text,'xml')

print(soup.find('div',class_='that not present in html content'))
