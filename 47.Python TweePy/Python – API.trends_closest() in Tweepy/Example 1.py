# import the module
import tweepy

# assign the values accordingly
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# coordinates of Delhi
lat = 28
long = 77

# fetching the locations
locations = api.trends_closest(lat, long)

print(str(len(locations)) + " location(s) is / are fetched.")
print("\nThe location(s) is / are :")
for location in locations:
	print(location['name'])
