item = 0
# Loop to go through each organisation
for link in orgLink:

	# Gets the anchor tag's hyperlink
	presentLink = link.get('href')

	url2 = 'https://summerofcode.withgoogle.com' + presentLink
	print(item)
	print(url2)
	orgURL[item] = url2
	res2 = requests.get(url2)
	res2.raise_for_status()

	soup2 = bs4.BeautifulSoup(res2.text, 'html.parser')
	tech = soup2.find_all("li",
					class_="organization__tag organization__tag--technology")

	# Finding if the org uses
	# the specified language
	for name in tech:

		if language in name.getText():
			languageCheck[item] = 'yes'

	item = item + 1
