# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'Q' represents quarter end frequency
idx = pd.DatetimeIndex(start ='2000-01-15 08:00', freq ='Q',
						periods = 4, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
