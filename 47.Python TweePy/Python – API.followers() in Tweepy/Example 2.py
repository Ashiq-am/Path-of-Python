# the screen_name of the targeted user
import tweepy

screen_name = "geeksforgeeks"

# getting only 30 followers
for follower in tweepy.Cursor(tweepy.api.followers, screen_name).items(30):
	print(follower.screen_name)
