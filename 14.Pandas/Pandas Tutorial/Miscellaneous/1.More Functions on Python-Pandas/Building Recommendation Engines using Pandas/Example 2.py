pop_movies = movies_merge.groupby("title")
pop_movies["user_id"].count().sort_values(
	ascending=False).reset_index().rename(
columns={"user_id": "score"})

pop_movies['Rank'] = pop_movies['score'].rank(
ascending=0, method='first')
pop_movies
