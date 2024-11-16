# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'MS' represents month start frequency
didx = pd.date_range(pd.Timestamp("2000-01-15 08:00"),
							periods = 5, freq ='MS')

# Print the DatetimeIndex
print(didx)
