import yfinance
ticker = "MSFT"
microsoft = yfinance.Ticker(ticker)
hist = microsoft.history(period="1mo")
print(hist['Close'])
