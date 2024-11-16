corr_Star_Wars_count[corr_Star_Wars_count[
'rating_counts'] > 100].sort_values(
	'Correlation', ascending=False).head()
corr_Star_Wars_count = corr_Star_Wars_count.reset_index()
corr_Star_Wars_count
