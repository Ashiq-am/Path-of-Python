# importing the module
import praw
from datetime import datetime

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

# fetching the Unix time of creation
unix_time = redditor.created_utc

print("The " + redditor_name + " account was created on Unix time : " +
	str(unix_time))

# converting the Unix time
print("The " + redditor_name + " account was created on : " +
	str(datetime.fromtimestamp(unix_time)))
