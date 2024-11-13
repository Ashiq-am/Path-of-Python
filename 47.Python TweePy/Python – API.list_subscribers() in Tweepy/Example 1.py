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

# the slug of the list
slug = "thought-leaders"

# the sceen name of the owner of the list
owner_screen_name = "kitson"

# fetching the subscribers
subscribers = api.list_subscribers(slug = slug,
								owner_screen_name = owner_screen_name)

# printing the screen names of the subscribers
for subscriber in subscribers:
	print(subscriber.screen_name)
