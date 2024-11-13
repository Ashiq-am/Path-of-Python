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

# the name of the media file
filename = "gfg.png"

# upload the file
media = api.media_upload(filename)

# printing the information
print("The media ID is : " + media.media_id_string)
print("The size of the file is : " + str(media.size) + " bytes")
