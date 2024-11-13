# parsing
url_link = requests.get(URL)
file = bs.BeautifulSoup(url_link.text, "lxml")
