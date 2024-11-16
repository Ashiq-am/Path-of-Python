# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data=['06:05:01.000030','+23:59:59.999999',
						'22 day 2 min 3us 10ns','+23:29:59.999999',
						'+12:19:59.999999'])

# Print the TimedeltaIndex object
print(tidx)
