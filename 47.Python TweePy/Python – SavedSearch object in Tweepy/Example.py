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

# the ID of the saved search
id = 1272422627047378944

# fetching the saved search
saved_search = api.get_saved_search(id)

# printing the information
print("The id of the saved search is : " + str(saved_search.id))
print("The id_str of the saved search is : " + saved_search.id_str)
print("The query of the saved search is : " + saved_search.query)
print("The name of the saved search is : " + saved_search.name)
print("The position of the saved search is : " + str(saved_search.position))
print("The saved search was created at : " + str(saved_search.created_at))
