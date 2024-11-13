import tweepy

# Define a class inheriting from StreamListener to handle the incoming stream of tweets
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

# Authenticate to the Twitter API using your credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an instance of the stream listener and start streaming tweets
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth, listener=myStreamListener)
myStream.filter(track=['python'])
