pd.cut(df.Year,
	bins=pd.interval_range(start=2002.99,
							end=2018,
							periods=3)).head()
