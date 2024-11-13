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

# the screen name of the owner of the list
owner_screen_name = "Ashiqul Amin"

# the ID of the list
list_id = "Ashiq"

# deleting the list
api.destroy_list(owner_screen_name, list_id = list_id)
