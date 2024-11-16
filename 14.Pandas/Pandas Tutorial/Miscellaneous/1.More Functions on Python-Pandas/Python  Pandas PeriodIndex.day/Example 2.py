# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2011-03-14 ',
			end ='2011-03-21', freq ='D')

# Print the PeriodIndex object
print(pidx)
