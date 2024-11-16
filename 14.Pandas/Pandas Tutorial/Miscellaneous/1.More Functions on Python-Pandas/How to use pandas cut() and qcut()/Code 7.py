pd.cut(df.Year, bins=3,
	labels=['old', 'medium', 'new']).head()
