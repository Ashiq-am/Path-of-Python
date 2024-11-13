# the ID of the tweet
ID = 1263387365051183107

# number to retweets to be retrieved
count = 3

# getting the retweeters
retweets_list = api.retweets(ID, count)

# printing the screen names of the retweeters
for retweet in retweets_list:
	print(retweet.user.screen_name)
