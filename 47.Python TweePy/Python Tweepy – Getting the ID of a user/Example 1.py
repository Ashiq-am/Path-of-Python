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

# the screen name of the user
screen_name = "geeksforgeeks"

# fetching the user
user = api.get_user(screen_name)

# fetching the ID
ID = user.id_str

print("The ID of the user is : " + ID)
