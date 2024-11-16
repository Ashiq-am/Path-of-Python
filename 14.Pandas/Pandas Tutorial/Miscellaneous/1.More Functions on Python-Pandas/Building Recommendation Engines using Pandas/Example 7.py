ratings_mean_count_data = pd.DataFrame(
	movies_merge.groupby('title')['rating'].mean())
ratings_mean_count_data['rating_counts'] = pd.DataFrame(
	movies_merge.groupby('title')['rating'].count())
ratings_mean_count_data
