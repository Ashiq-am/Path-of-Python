htmldata = getdata("https://barcindia.co.in/data-insights")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
for i in soup.find_all('tbody'):
    data = data + (i.get_text())

data
