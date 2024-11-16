# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
didx = pd.DatetimeIndex(start ='2000-01-31 06:30', freq ='BM',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
