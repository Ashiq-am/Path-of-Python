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

# Twitter ID of London
id = "457b4814b4240d87"

# fetching the location
location = api.geo_id(id)

# printing the information
print("Place Type : " + location.place_type)
print("Name : " + location.name)
print("Full Name : " + location.full_name)
print("Country : " + location.country)
