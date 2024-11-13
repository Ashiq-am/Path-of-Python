soup = BeautifulSoup(html,
					'html.parser')
temperature = soup.find(
'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
time_sky = soup.find(
'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
sky = time_sky.split('\n')[1]
