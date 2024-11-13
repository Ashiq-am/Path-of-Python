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

print("The number of saved searches before destroy_saved_search() : ", end = "")
print(len(api.saved_searches()))

# query of the saved search
id = 1269510986496569349

# deleting the saved search
api.destroy_saved_search(id)

print("The number of saved searches after destroy_saved_search() : ", end = "")
print(len(api.saved_searches()))
