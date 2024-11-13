import requests
from bs4 import BeautifulSoup as bs

link = "https://www.flipkart.com/watches/pr?sid=r18"
url = requests.get(link)
soup = bs(url.text)
elements = soup.find_all("div",class_="_1AtVbE col-12-12")
for element in elements:
	if element:
		a = element.find("div", class_="_13oc-S _1t9ceu")
if a:
	b = a.find("div", class_="_1xHGtK _373qXS")
	if b:
		c = b.find("div", class_="_2B099V")
		if c:
			d = c.find("div", class_="_25b18c")
			if d:
				e = d.find("div", class_="_30jeq3")
				print(e.text)
