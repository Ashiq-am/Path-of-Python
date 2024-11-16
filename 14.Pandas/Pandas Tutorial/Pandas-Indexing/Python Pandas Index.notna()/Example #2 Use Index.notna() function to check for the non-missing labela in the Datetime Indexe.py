# importing pandas as pd
import pandas as pd

# Creating the Datetime Index
idx = pd.DatetimeIndex([pd.Timestamp('2015-02-11'),
					None, pd.Timestamp(''), pd.NaT])

# Print the Datetime Index
idx
