from pyshorteners import Shortener

ACCESS_TOKEN = '82e8156..e4e12c6'

url = 'http://www.google.com'
url_shortener = Shortener('Bitly', bitly_token = ACCESS_TOKEN)

print ("Short URL is {}".format(url_shortener.short(url)))
