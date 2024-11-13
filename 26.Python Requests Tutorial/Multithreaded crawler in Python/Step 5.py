def scrape_page(self, url):
	try:
		res = requests.get(url, timeout=(3, 30))
		return res
	except requests.RequestException:
		return
