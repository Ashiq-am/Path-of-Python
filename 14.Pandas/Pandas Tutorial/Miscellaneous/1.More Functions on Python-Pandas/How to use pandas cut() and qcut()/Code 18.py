# demonstrating with some random quantiles
pd.qcut(df.Year, q=[0,0.15,0.35,
					0.51,0.78,1]).head()
