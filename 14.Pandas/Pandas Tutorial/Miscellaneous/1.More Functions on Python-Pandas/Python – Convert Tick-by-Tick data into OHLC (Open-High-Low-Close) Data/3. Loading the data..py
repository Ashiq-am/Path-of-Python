data_ask = data_frame['Ask'].resample('15Min').ohlc()
data_bid = data_frame['Bid'].resample('15Min').ohlc()
