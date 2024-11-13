# the screen_name of the targeted user
import tweepy

screen_name = "geeksforgeeks"

# getting all the followers
c = tweepy.Cursor(tweepy.api.followers, screen_name)

# counting the number of followers
count = 0
for follower in c.items():
	count += 1
print(screen_name + " has " + str(count) + " followers.")
