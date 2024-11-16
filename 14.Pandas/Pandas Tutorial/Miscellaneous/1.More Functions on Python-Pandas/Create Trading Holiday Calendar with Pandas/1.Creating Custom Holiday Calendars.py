import pandas as pd
import holidays

# Define the trading holidays for the Indian market
us_holidays = holidays.India(years=[2023])

# additional holidays
additional_holidays = [
    '2023-01-26',  # Republic Day
    '2023-08-15',  # Independence Day
    '2023-10-02',  # Gandhi Jayanti
]

# Generate a date range for the entire year
# 'B' is business days
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')

# Convert the holiday list to a Pandas Series
holiday_dates = pd.to_datetime([date for date in us_holidays] + additional_holidays)

# Filter out the holidays from the date range
trading_days = date_range[~date_range.isin(holiday_dates)]

# Print the trading days
print(trading_days)
