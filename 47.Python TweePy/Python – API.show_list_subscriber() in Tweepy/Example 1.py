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

# the ID of the list
list_id = 4343

# screen name of the user to be checked
screen_name = "LiptakCarl"

# checking if the user is subscribed to the list
api.show_list_subscriber(list_id = list_id, screen_name = screen_name)

# if no exception is raised then the user is subscribed to the list
print("The user " + screen_name + " is subscribed to the list " +
	api.get_list(list_id = list_id).name)
