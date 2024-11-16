# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2005-12-21',
			end ='2005-12-29', freq ='D')

# Print the PeriodIndex object
print(pidx)
