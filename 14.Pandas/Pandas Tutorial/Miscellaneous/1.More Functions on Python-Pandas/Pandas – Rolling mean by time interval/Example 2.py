# importing Data
tesla_df = pd.read_csv('Tesla_Stock.csv', index_col='Date',
					parse_dates=True)

# printing the dataFrame
tesla_df.head(10)
