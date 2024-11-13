import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep

URL = 'https://www.geeksforgeeks.org/page/'

for page in range(1,10):
	# pls note that the total number of
	# pages in the website is more than 5000 so i'm only taking the
	# first 10 as this is just an example

	req = requests.get(URL + str(page) + '/')
	soup = bs(req.text, 'html.parser')

	titles = soup.find_all('div',attrs={'class','head'})

	for i in range(4,19):
		if page>1:
			print(f"{(i-3)+page*15}" + titles[i].text)
		else:
			print(f"{i-3}" + titles[i].text)

	sleep(randint(2,10))
