print(movies_merge.groupby('title')[
	'rating'].mean().sort_values(
ascending=False).head())

print(movies_merge.groupby('title')[
	'rating'].count().sort_values(
ascending=False).head())
