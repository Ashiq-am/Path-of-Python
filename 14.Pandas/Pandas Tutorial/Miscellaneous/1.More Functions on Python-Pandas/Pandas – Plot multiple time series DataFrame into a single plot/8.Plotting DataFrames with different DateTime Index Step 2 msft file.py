# importing Data
msft = pd.read_csv('msft.csv',
				index_col='Date',
				parse_dates=True)
# printing 10 entries of the data
msft.head(10)
