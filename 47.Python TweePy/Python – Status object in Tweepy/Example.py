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

# the ID of the status
id = 1268080321590935553

# fetching the status
status = api.get_status(id)

# printing the information
print("The status was created at : " + str(status.created_at))
print("The id is : " + str(status.id))
print("The id_str is : " + status.id_str)
print("The text is : " + status.text)
print("The entitities are : " + str(status.entities))
print("The source is : " + status.source)
print("The source_url is : " + status.source_url)


print("The in_reply_to_status_id is : " + str(status.in_reply_to_status_id))
print("The in_reply_to_status_id_str is : " + str(status.in_reply_to_status_id_str))
print("The in_reply_to_user_id is : " + str(status.in_reply_to_user_id))
print("The in_reply_to_user_id_str is : " + str(status.in_reply_to_user_id_str))
print("The in_reply_to_screen_name is : " + str(status.in_reply_to_screen_name))


print("The poster's screen name is : " + status.user.screen_name)
print("The geo is : " + str(status.geo))
print("The coordinates are : " + str(status.coordinates))
print("The place is : " + str(status.place))
print("The contributors are : " + str(status.contributors))
print("The is_quote_status is : " + str(status.is_quote_status))
print("The retweet_count is : " + str(status.retweet_count))
print("The favorite_count is : " + str(status.favorite_count))

print("Has the authenticated user favourited the status? : " + str(status.favorited))
print("Has the authenticated user retweeted the status? " + str(status.retweeted))
print("Is the status possibly_sensitive? : " + str(status.possibly_sensitive))
print("The lang is : " + status.lang)
