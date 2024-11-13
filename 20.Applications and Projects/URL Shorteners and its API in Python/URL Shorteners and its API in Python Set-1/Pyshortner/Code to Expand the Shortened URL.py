from pyshorteners import Shortener

short_url ='https://goo.gl/fbsS'

API_Key = 'AIzaSyBBSL...jXKIGh1fNU'

url_expander = Shortener('Google', api_key = API_Key)

print ("Long URL is {}".format(url_expander.expand(short_url)))
