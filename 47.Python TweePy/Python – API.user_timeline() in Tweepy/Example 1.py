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

# screen name of the account to be fetched
screen_name = "geeksforgeeks"

# fetching the statuses
statuses = api.user_timeline(screen_name)

print(str(len(statuses)) + " number of statuses have been fetched.")
