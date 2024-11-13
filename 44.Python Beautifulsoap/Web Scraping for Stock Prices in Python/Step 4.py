all = []
for url in urls:
    page = requests.get(url, headers=headers)
    try:
        soup = BeautifulSoup(page.text,
                             'html.parser')
        company = soup.find('h1', {'class':
                                       'text-2xl font-semibold \
                                       instrument-header_title__gCaMF \
                                       mobile:mb-2'}).text
        price = soup.find('div', {'class':
                                      'instrument-price_instrument-price__xfgbB flex \
                                      items-end flex-wrap font-bold'}).find_all('span')[0].text
        change = soup.find('div', {'class':
                                   'instrument-price_instrument-price__xfgbB \
                                   flex items-end flex-wrap font-bold'}).find_all('span')[2].text

        volume = soup.find('div', {'class':
                               'trading-hours_value__5_NnB'}).text

        x = [company, price, change, volume]

        all.append(x)

    except AttributeError:
        print("Change the Element id")
