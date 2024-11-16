# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start='2005-12-21 08:45 ',
			end='2005-12-21 11:55', freq='H')

# Print the PeriodIndex object
print(pidx)
