# code
aapl = pd.read_csv('aapl.csv',
				index_col='Date',
				parse_dates=True)
# printing 10 entries of the data
aapl.head(10)
