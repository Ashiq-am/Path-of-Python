from pyshorteners import Shortener

# uid means User Id and key means API Key.
url = 'http://www.google.com'

url_shortener = Shortener('Adfly', uid ='20727891', key ='b8de8e0...5a2381241c', type ='int')

print ("Short URL is {}".format(url_shortener.short(url)))
