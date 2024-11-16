# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data =['-1 days 2 min 3us 10ns', '1 days 06:05:01.000030',
													'-1 days + 23:59:59.999999'])

# Print the TimedeltaIndex
print(tidx)
