# Function to extract html data
def getdata(url):
	r=requests.get(url)
	return r.text
