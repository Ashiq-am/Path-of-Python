import pandas as pd
import holidays
import yfinance as yf

# Define the trading holidays for the US market (NYSE)
us_holidays = holidays.UnitedStates(years=[2023])


# Generate a date range for the entire year
# 'B' is business days
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')

# Convert the holiday list to a Pandas Series
holiday_dates = pd.to_datetime([date for date in us_holidays])

# Filter out the holidays from the date range
trading_days = date_range[~date_range.isin(holiday_dates)]

# Download stock data using yfinance
ticker = 'AAPL'
stock_data = yf.download(ticker, start='2023-01-01', end='2023-12-31')

# Filter the stock data based on the trading holiday calendar
filtered_stock_data = stock_data.loc[stock_data.index.isin(trading_days)]

# Display the filtered stock data
print(filtered_stock_data.head())
