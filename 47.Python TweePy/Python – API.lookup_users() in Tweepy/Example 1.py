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

# list of user_ids
user_ids = [57741058, 4802800777, 1037141442]

# getting the users by user_ids
users = api.lookup_users(user_ids)

# printing the user details
for user in users:
	print("The id is : " + str(user.id))
	print("The screen name is : " + user.screen_name, end = "\n\n")
