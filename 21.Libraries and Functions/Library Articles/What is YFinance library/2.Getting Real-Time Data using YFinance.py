import yfinance as yf

# Define the ticker symbol
ticker = 'AAPL'

# Get the ticker object
stock = yf.Ticker(ticker)

# Get real-time price data
price = stock.history(period="1d")['Close'][0]
print(f"Real-time price for {ticker}: {price}")
