# import packages
import pandas as pd

# unit='ms' to calculate the number
# of milliseconds
date = pd.to_datetime(1550767605,
					unit = 'ms')

# checking our dataframe once again
print(date)
