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

# fetching the saved searches
saved_searches = api.saved_searches()

# printing the information
for saved_search in saved_searches:
	print("The ID of this saved search is : " + str(saved_search.id))
	print("The query of this saved search is : " + saved_search.query, end = "\n\n")
