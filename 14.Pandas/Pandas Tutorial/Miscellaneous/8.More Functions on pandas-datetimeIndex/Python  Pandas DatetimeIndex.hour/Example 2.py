# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here the 'H' represents hourly frequency
didx = pd.DatetimeIndex(start ='2000-01-10 06:30', freq ='H',
							periods = 3, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
