# the ID of the status
id = 1272479136133627905

# fetching the status with extended tweet_mode
status = api.get_status(id, tweet_mode = "extended")

# fetching the retweet_count attribute
retweet_count = status.retweet_count

print("The number of time the status has been retweeted is : " + str(retweet_count))
