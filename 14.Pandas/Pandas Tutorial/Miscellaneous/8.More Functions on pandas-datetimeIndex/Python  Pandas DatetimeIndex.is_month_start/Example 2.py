# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
didx = pd.DatetimeIndex(start ='2000-01-10 06:30', freq ='CBMS',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
