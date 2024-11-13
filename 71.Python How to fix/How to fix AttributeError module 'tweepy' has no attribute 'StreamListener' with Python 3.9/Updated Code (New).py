# Upgrade tweepy to the latest version
#!pip install tweepy --upgrade

import tweepy

# Define a class inheriting from StreamingClient to handle the incoming stream of tweets
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet): # Use on_tweet to process incoming tweets
        print(tweet.text)

# Authenticate to the Twitter API using your credentials (replace placeholders with your actual keys)
bearer_token = "YOUR_BEARER_TOKEN" # You'll need a bearer token for StreamingClient

# Create an instance of the stream and start streaming tweets
myStream = MyStream(bearer_token)
myStream.add_rules(tweepy.StreamRule("python")) # Add rules to filter tweets
myStream.filter()
