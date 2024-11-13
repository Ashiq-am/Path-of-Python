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

# ID of the recipient
recipient_id = ""

# text to be sent
text = "This is a Direct Message."

# sending the direct message
direct_message = api.send_direct_message(recipient_id, text)

# printing the text of the sent direct message
print(direct_message.message_create['message_data']['text'])
