movies_merge = pd.merge(ratings, movies,
						on='item_id')
movies_merge.head()
