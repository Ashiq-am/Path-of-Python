# importing time-series data
reliance = pd.read_csv('RELIANCE.NS.csv',
					index_col='Date',
					parse_dates=True)

# Printing dataFrame
reliance.head()
