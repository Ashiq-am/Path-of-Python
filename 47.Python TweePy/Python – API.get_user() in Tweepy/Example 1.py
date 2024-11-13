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

# using get_user with id
_id = "103770785"
user = api.get_user(_id)

# printing the name of the user
print("The id " + _id +
	" corresponds to the user with the name : " +
	user.name)
