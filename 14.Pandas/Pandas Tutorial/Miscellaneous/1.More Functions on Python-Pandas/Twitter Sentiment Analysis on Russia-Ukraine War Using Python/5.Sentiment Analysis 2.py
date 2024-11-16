total_pos = len(tweets.loc[tweets['sentiment'] == "positive"])
total_neg = len(tweets.loc[tweets['sentiment'] == "negative"])
total_neu = len(tweets.loc[tweets['sentiment'] == "neutral"])
total_tweets = len(tweets)
print("Total Positive Tweets % : {:.2f}"
	.format((total_pos/total_tweets)*100))
print("Total Negative Tweets % : {:.2f}"
	.format((total_neg/total_tweets)*100))
print("Total Neutral Tweets % : {:.2f}"
	.format((total_neu/total_tweets)*100))
