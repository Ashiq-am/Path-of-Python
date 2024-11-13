# import module
from gnewsclient import gnewsclient

# declare a NewsClient object
client = gnewsclient.NewsClient(language='hindi', location='india', topic='Business', max_results=5)

# get news feed
client.get_news()
