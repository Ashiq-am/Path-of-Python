from pyshorteners import Shortener
ACCESS_TOKEN = '82e8156...c1dce4e12c6'

url = 'http://bit.ly/2OGRcfW'
url_expander = Shortener('Bitly', bitly_token = ACCESS_TOKEN)

print ("Long URL is {}".format(url_expander.expand(url)))
