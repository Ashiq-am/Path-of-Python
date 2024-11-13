# method to get the price of silver
def silver_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/silver-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding metha info for the current price
	price = soup.find("div", class_="gold_silver_table right-align-content").find(
		"tr", class_="odd_row").findAll("td")

	# returnng the price in text
	return price[1].text


# method to get the price of gold
def gold_price():

	# getting the request from url
	data = requests.get(
		"https://www.goodreturns.in/gold-rates/#Today+24+Carat+Gold+Rate+Per+Gram+in+India+%28INR%29")

	# converting the text
	soup = BeautifulSoup(data.text, 'html.parser')

	# finding metha info for the current price
	price = soup.find("div", class_="gold_silver_table right-align-content").find(
		"tr", class_="odd_row").findAll("td")

	# returnng the price in text
	return price[1].text
