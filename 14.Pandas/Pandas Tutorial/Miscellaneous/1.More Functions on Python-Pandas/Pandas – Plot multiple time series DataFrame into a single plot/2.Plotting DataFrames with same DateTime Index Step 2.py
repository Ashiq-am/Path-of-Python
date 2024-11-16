# code
# importing Data
tesla = pd.read_csv('Tesla_Stock.csv',
					index_col='Date',
					parse_dates=True)
tesla.head(10)
