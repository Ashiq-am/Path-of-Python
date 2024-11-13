# parsing
soup = BeautifulSoup(contents, 'xml')
titles = soup.find_all('title')
