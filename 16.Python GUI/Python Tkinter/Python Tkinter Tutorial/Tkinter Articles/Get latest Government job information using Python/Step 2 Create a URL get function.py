import requests


def getdata(url):
	r = requests.get(url)
	return r.text
