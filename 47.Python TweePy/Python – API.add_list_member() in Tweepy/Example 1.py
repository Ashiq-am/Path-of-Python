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
list_id = ''

# screen name of the user to be added
screen_name = "geeksforgeeks"

print("Number of members before add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))

# adding the user to the list
api.add_list_member(list_id = list_id, screen_name = screen_name)

print("Number of members after add_list_member() is used : " +
	str(api.get_list(list_id = list_id).member_count))
