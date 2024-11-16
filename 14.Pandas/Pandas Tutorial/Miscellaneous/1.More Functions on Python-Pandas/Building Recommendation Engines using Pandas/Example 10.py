movies_like_Star_Wars = user_rating.corrwith(Star_Wars_ratings)

corr_Star_Wars = pd.DataFrame(movies_like_Star_Wars,
							columns=['Correlation'])
corr_Star_Wars.dropna(inplace=True)
corr_Star_Wars.head(10)
corr_Star_Wars.sort_values('Correlation',
						ascending=False).head(25)
