# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2003-12-21 08:45 ',
			end ='2003-12-21 8:55', freq ='T')

# Print the PeriodIndex object
print(pidx)
