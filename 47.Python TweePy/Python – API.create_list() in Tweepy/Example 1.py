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

# name of the list
name = "tweepy_list"

# creating the list
list = api.create_list(name)

print("Name of the list : " + list.name)
print("Number of members in the list : " + str(list.member_count))
print("Mode of the list : " + list.mode)
