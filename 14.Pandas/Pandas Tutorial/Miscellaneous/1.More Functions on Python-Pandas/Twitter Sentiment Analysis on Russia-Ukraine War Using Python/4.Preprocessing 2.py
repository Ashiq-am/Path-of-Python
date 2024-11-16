# before removing the non-english tweets
print(tweets.shape)

# removing all the tweets expect the
# non-english tweets
tweets = tweets[tweets['lang'] == 'en']
print("After removing non-english Tweets")

# only the number of english tweets
print(tweets.shape)
