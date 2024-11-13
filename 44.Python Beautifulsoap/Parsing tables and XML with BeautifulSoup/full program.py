# import required modules
import bs4 as bs
import requests

# assign URL
URL = 'https://www.geeksforgeeks.org/python-list/'

# parsing
url_link = requests.get(URL)
file = bs.BeautifulSoup(url_link.text, "lxml")

# find all tables
find_table = file.find('table', class_='numpy-table')
rows = find_table.find_all('tr')

# display tables
for i in rows:
	table_data = i.find_all('td')
	data = [j.text for j in table_data]
	print(data)
