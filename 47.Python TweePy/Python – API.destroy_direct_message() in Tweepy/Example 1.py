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

# direct message ID
id = print("Before using the destroy_direct_message() object")
if api.get_direct_message(id):
	print("This direct message exists.")

# deleting the direct message
api.destroy_direct_message(id)


print("\nAfter using the destroy_direct_message() object")
try:
	api.get_direct_message(id)
except:
	print("This direct message no longer exists.")
