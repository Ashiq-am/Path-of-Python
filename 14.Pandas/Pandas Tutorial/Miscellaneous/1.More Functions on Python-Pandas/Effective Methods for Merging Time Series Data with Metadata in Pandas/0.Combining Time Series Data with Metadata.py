import pandas as pd

# Sample time series data (stock prices)
stock_data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'AAPL': [150.25, 152.10, 153.50],
    'GOOGL': [2800.50, 2825.75, 2850.00]
})

# Sample metadata (company information)
metadata = pd.DataFrame({
    'Ticker': ['AAPL', 'GOOGL'],
    'Company': ['Apple Inc.', 'Alphabet Inc.']
})

# Transpose stock_data to have 'Ticker' as a column
stock_data = stock_data.melt(id_vars=['Date'], var_name='Ticker', value_name='Price')

# Merge time series data with metadata based on common key (Ticker)
combined_data = pd.merge(stock_data, metadata, on='Ticker')
print(combined_data)
