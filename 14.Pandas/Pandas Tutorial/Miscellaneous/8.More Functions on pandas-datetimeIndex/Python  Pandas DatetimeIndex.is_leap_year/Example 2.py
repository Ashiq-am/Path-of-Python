# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
didx = pd.date_range("2008-12-30", periods = 5, freq ='Q')

# Print the DatetimeIndex
print(didx)
