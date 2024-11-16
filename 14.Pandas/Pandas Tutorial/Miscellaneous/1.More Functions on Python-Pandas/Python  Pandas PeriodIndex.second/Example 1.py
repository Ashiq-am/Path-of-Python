# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2004-11-21 08:45:21 ',
			end ='2004-11-21 8:45:29', freq ='S')

# Print the PeriodIndex object
print(pidx)
