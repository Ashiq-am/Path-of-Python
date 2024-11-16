# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'S' represents secondly frequency
didx = pd.DatetimeIndex(start ='2000-01-15 08:00', freq ='S', periods = 4)

# Print the DatetimeIndex
print(didx)
