url = 'https://finance.yahoo.com/cryptocurrencies/'
response = requests.get(url)
text = response.text
data = BeautifulSoup(text, 'html.parser')
