pd.cut(df.Year, bins=[2003,
					2007,
					2010,
					2015,
					2018],
	include_lowest=True).head()
