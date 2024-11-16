# code
# importing data
ford = pd.read_csv('Ford_Stock.csv',
				index_col='Date',
				parse_dates=True)
ford.head(10)
