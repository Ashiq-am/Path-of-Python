# code
# importing data
gm = pd.read_csv('GM_Stock.csv',
				index_col='Date',
				parse_dates=True)
# printing 10 entries of the data
gm.head(10)
