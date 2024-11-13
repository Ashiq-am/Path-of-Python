# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url)
	return r.text
