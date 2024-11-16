# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx1 = pd.TimedeltaIndex(data =['1 days 02:00:00', '1 days 06:05:01.000030',
								'1 days 02:00:00', '1 days 02:00:00',
								'21 days 06:15:01.000030'])

# Create the second TimedeltaIndex object
tidx2 = pd.TimedeltaIndex(data =['06:05:01.000030', '+23:59:59.999999',
								'22 day 2 min 3us 10ns', '+12:19:59.999999'])

# Print the first and second TimedeltaIndex object
print(tidx1, "\n", tidx2)
