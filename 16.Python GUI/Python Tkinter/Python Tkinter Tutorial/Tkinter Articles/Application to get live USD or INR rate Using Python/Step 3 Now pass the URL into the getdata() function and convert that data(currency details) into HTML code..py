# Extract and convert
htmldata = getdata("https://finance.yahoo.com/quote/usdinr=X?ltr=1")
soup = BeautifulSoup(htmldata, 'html.parser')
result = (soup.find_all("div", class_="D(ib) Va(m) Maw(65%) Ov(h)"))
