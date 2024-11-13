import praw
import pandas as pd

reddit_read_only = praw.Reddit(client_id="",		 # your client id
							client_secret="",	 # your client secret
							user_agent="")	 # your user agent

# URL of the post
url = "https://www.reddit.com/r/IAmA/comments/m8n4vt/\
im_bill_gates_cochair_of_the_bill_and_melinda/"

# Creating a submission object
submission = reddit_read_only.submission(url=url)
