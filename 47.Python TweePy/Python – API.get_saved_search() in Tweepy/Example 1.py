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

# ID of the saved search
id = 1269503225993900032

# fetching the saved search
saved_search = api.get_saved_search(id)

# printing the information
print("The ID of the saved search is : " + str(saved_search.id))
print("The query of this saved search is : " + saved_search.query)
