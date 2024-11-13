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

# the ID of the comment
comment_id = "fvib7aw"

# instantiating the Comment class
comment = reddit.comment(comment_id)

# fetching the link_id attribute
link_id = comment.link_id

print("The submission ID of the comment is : " + link_id)
