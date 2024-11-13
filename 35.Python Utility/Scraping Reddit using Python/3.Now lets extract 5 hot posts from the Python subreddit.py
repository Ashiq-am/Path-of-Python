subreddit = reddit_read_only.subreddit("Python")

for post in subreddit.hot(limit=5):
	print(post.title)
	print()
