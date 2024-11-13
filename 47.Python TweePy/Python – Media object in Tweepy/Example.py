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

# uploading the media and fetching the Media object
media = api.media_upload("gfg.png")

# printing the information
print("The media_id is : " + str(media.media_id))
print("The media_id_string is : " + media.media_id_string)
print("The size is : " + str(media.size))
print("The expires_after_secs is : " + str(media.expires_after_secs))
print("The image_type is : " + str(media.image["image_type"]))
print("The w is : " + str(media.image["w"]))
print("The h is : " + str(media.image["h"]))
