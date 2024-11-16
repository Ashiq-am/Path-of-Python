pd.qcut(df.Year,
		q=[0, 0.2, 0.4,
		0.6, 0.8, 1.0],
		labels=['oldest',
				'not so old',
				'medium',
				'newer',
				'latest']).value_counts()
