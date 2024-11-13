''''''


'''Following code depicts how other factors like location, language and topic can be 
printed from information collected by this module'''



import gnewsclient
from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(language='hindi',
								location='india',
								topic='Business',
								max_results=5)

# prints location
print("Location: \n",client.locations)
print()

# prints languages
print("Language \n",client.languages)
print()

# prints topics
print("Topic \n",client.topics)
