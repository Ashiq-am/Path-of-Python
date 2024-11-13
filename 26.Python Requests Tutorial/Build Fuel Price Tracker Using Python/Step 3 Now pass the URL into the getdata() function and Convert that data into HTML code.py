# link for extract html data
htmldata = getdata("https://www.goodreturns.in/petrol-price.html")
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all("div", class_="gold_silver_table")
print(result)
