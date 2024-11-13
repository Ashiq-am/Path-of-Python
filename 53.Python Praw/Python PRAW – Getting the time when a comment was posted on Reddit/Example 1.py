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
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# the ID of the comment
comment_id = "fvib7aw"

# instantiating the Comment class
comment = reddit.comment(comment_id)

# fetching the Unix time
unix_time = comment.created_utc

print("The comment was posted on Unix time : " +
      str(unix_time))

# converting the Unix time
print("The comment was posted on : " +
      str(datetime.fromtimestamp(unix_time)))
