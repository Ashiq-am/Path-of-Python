import yfinance as yahooFinance


GetFacebookInformation = yahooFinance.Ticker("FB")

# Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y,
# 2y, 5y, 10y and ytd.
print(GetFacebookInformation.history(period="6mo"))
