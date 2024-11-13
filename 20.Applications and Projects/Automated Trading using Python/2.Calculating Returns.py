# Import numpy package
import numpy as np


# assign `Adj Close` to `close_price`
close_price = msft_data[['Adj_Close']]

# returns as fractional change
daily_return = close_price.pct_change()

# replacing NA values with 0
daily_return.fillna(0, inplace=True)

print(daily_return)
