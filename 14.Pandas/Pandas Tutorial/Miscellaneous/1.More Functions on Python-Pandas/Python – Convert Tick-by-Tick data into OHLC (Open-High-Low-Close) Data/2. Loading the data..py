data_frame = pd.read_csv(
	'AUDJPY-2016-01.csv', names=['Symbol', 'Date_Time', 'Bid', 'Ask'],
									index_col=1, parse_dates=True)
data_frame.head()
