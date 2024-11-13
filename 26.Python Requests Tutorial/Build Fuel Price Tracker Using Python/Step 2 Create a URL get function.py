# user define function
# Scrape the data
import requests


def getdata(url):
	r = requests.get(url)
	return r.text
