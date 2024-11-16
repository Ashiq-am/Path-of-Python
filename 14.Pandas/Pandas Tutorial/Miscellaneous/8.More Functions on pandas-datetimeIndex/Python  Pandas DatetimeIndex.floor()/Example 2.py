# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'T' represents minutely frequency
didx = pd.DatetimeIndex(start ='2000-01-15 08:00', freq ='T', periods = 4)

# Print the DatetimeIndex
print(didx)
