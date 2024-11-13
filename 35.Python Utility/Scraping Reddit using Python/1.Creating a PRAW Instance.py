# Read-only instance
reddit_read_only = praw.Reddit(client_id="",		 # your client id
							client_secret="",	 # your client secret
							user_agent="")	 # your user agent

# Authorized instance
reddit_authorized = praw.Reddit(client_id="",		 # your client id
								client_secret="",	 # your client secret
								user_agent="",	 # your user agent
								username="",	 # your reddit username
								password="")	 # your reddit password
