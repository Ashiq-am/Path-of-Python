# importing the module
import praw

# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

# creating an authorized reddit instance
reddit = praw.Reddit(client_id = client_id,
					client_secret = client_secret,
					username = username,
					password = password,
					user_agent = user_agent)

# the name of the redditor
redditor_name = "AutoModerator"

# instantiating the Redditor class
redditor = reddit.redditor(redditor_name)

# before using the friend() method
print("Are the authenticated user and " + redditor.name +
	" friends? : " + str(redditor.is_friend))

# befriending the redditor
redditor.friend()

# after using the friend() method
print("Are the authenticated user and " + redditor.name +
	" friends? : " + str(redditor.is_friend))
