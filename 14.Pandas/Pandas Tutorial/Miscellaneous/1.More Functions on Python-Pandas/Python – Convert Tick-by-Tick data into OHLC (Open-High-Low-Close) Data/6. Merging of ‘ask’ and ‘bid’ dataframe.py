data_ask_bid = pd.concat(
	[data_ask, data_bid], axis=1,
	keys=['Ask', 'Bid'])
