# import module
import requests
import pandas as pd
from bs4 import BeautifulSoup


res = ''

# link for extract html data
def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://www.sarkariresult.com/latestjob.php")
soup = BeautifulSoup(htmldata, 'html.parser')

for li in soup.find_all("div", id="post"):
	res += (li.get_text())

print(res)
