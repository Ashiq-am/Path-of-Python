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

# ID of the direct message
id = 1271013844639313927

# fetching the direct message
direct_message = api.get_direct_message(id)

# printing the information
print("The type is : " + direct_message.type)
print("The id is : " + direct_message.id)
print("The created_timestamp is : " + direct_message.created_timestamp)

# inside message_create
print("The recipient_id is : " + direct_message.message_create['target']['recipient_id'])
print("The sender_id is : " + direct_message.message_create['sender_id'])
print("The source_app_id is : " + direct_message.message_create['source_app_id'])
print("The text is : " + str(direct_message.message_create['message_data']['text']))
print("The entities are : " + str(direct_message.message_create['message_data']['entities']))
print("The media attachment is : " + str(direct_message.message_create['message_data']['attachment']))
