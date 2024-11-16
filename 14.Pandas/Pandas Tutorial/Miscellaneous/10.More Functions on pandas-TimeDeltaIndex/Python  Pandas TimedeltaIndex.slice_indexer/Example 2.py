# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(start ='03 days 09:22:56',
							periods = 5, freq ='H')

# Print the TimedeltaIndex object
print(tidx)
