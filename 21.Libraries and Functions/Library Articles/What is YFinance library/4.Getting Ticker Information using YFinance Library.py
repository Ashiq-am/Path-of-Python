import yfinance as yf

# Define the ticker symbol
ticker = 'AAPL'

# Get the ticker object
stock = yf.Ticker(ticker)

# Get basic information
info = stock.info
print(f"Company: {info['longName']}")
print(f"Sector: {info['sector']}")
print(f"Industry: {info['industry']}")
print(f"Market Cap: {info['marketCap']}")
print(f"P/E Ratio: {info['trailingPE']}")
