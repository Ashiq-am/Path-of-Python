from pyshorteners import Shortener

url = 'http://www.google.com'

url_shortener = Shortener('Dagd')

print ("Short URL is {}".format(url_shortener.short(url)))
