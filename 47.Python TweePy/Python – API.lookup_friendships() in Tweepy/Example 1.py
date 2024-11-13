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

# list of screen names
screen_names = ["SrBachchan",
				"akshaykumar",
				"imVkohli",
				"sachin_rt",
				"SonuSood"]

# getting the friendship details
friendships = api.lookup_friendships(screen_names = screen_names)

for friendship in friendships:
	print("Is the authenticated user following " + friendship.screen_name, end = "? : ")
	print(friendship.is_following)
