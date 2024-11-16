user_rating = movies_merge.pivot_table(
	index='user_id', columns='title', values='rating')
user_rating.head()
