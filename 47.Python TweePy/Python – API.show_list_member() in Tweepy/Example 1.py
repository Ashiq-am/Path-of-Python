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
list_id = ""


# the user to be checked in the list
screen_name = "geeksforgeeks"

# checking the user is present in the list or not
api.show_list_member(list_id = list_id, screen_name = screen_name)

# if there is no exception then the user is present
print("The user " + screen_name + " is present in the list.")
