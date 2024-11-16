pd.qcut(df.Selling_Price,
		q=np.arange(0, 1.01, 0.25),
		labels=['inexpensive',
				'average',
				'high cost',
				'over budget']).head()
