# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url, headers = HEADERS)
	return r.text
