import yfinance as yf

# Define the ticker symbol
ticker = 'AAPL'

# Get the ticker object
stock = yf.Ticker(ticker)

# Get dividends data
dividends = stock.dividends
print("Dividends:")
print(dividends.head())
