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

print("The number of saved searches before create_saved_search() : ", end = "")
print(len(api.saved_searches()))

# query of the new saved search
query = "Tweepy"

# creating the saved search
api.create_saved_search(query)

print("The number of saved searches after create_saved_search() : ", end = "")
print(len(api.saved_searches()))
