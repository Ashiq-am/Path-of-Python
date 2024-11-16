# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start = '2016-10-12 11:12:02',
			end = '2020-04-12 11:32:12', freq = 'Q')

# Print the PeriodIndex object
print(pidx)
