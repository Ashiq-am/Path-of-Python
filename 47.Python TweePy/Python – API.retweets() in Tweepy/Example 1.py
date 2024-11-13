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

# the ID of the tweet
ID = 1265889240300257280

# getting the retweeters
retweets_list = api.retweets(ID)

# printing the screen names of the retweeters
for retweet in retweets_list:
	print(retweet.user.screen_name)
