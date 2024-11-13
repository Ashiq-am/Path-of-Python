import yfinance as yahooFinance
GetFacebookInformation = yahooFinance.Ticker("FB")

# get all key value pairs that are available
for key, value in GetFacebookInformation.info.items():
	print(key, ":", value)
