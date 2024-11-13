# the screen_name of the targeted user
screen_name = "TwitterIndia"

# getting only 30 friends
for friend in tweepy.Cursor(api.friends, screen_name).items(30):
	print(friend.screen_name)
