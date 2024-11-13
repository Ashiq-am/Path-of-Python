from pyshorteners import Shortener

url = 'http://www.google.com'

url_shortener = Shortener('Osdb')

print ("SHORT URL is {}".format(url_shortener.short(url)))
