import yfinance as yf

# Define the ticker symbol
ticker = 'AAPL'

# Get historical market data
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

# Display the first few rows of the data
print(data.head())
