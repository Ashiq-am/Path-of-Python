import urllib.request
from bs4 import BeautifulSoup
url = input('Enter URL of Webpage: ')
print('\n')
url_request = urllib.request.Request(url)
url_response = urllib.request.urlopen(url)
webpage_data = url_response.read()
soup = BeautifulSoup(webpage_data, 'html.parser')
