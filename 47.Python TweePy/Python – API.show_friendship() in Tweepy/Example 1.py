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

# screen name of the account 1
source_screen_name = "Twitter"

# screen name of the account 2
target_screen_name = "TwitterIndia"

# getting the friendship details
friendship = api.show_friendship(source_screen_name = source_screen_name, target_screen_name = target_screen_name)

print("Is " + friendship[0].screen_name + " followed by " + friendship[1].screen_name, end = "? : ")
if friendship[0].followed_by == False:
	print("No")
else:
	print("Yes")

print("Is " + friendship[0].screen_name + " following " + friendship[1].screen_name, end = "? : ")
if friendship[0].following == False:
	print("No")
else:
	print("Yes")
