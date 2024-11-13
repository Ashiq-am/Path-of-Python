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

# the ID of the status
ID = 1263493041769394178

# deleting the status
api.destroy_status(ID)

# verifying if the status has
# been deleted or not
try:
	api.get_status(ID)
except:
	print("The status has been successfully deleted.")
