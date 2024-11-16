# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start = '2016-10-12 11:12:02',
			end = '2016-10-12 11:19:12', freq = 'T')

# Print the PeriodIndex object
print(pidx)
