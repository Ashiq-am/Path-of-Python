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

# fetching the list of moderated subreddits
subreddits = redditor.moderated()

# counting the number od subreddits moderated
print(redditor_name + " is a moderator of " + str(len(subreddits)) + " number of subreddits.")
