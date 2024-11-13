# the screen_name of the targeted user
import tweepy

screen_name = "geeksforgeeks"

# getting all the friends
c = tweepy.Cursor(api.friends, screen_name)

# counting the number of friends
count = 0
for friends in c.items():
	count += 1
print(screen_name + " has " + str(count) + " friends.")
