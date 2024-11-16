# importing pandas as pd
import pandas as pd

# Create the first TimedeltaIndex object
tidx1 = pd.TimedeltaIndex(data =['06:05:01.000030', '+23:59:59.999999',
								'22 day 2 min 3us 10ns', '+23:29:59.999999',
														'+12:19:59.999999'])

# Create the seccond TimedeltaIndex object
tidx2 = pd.TimedeltaIndex(data =['09:11:18.000030', '+23:59:59.999999',
								'9 day 18 min 3us ', '+23:29:59.999999',
													'+12:19:59.999999'])

# Print the first and second TimedeltaIndex object
print(tidx1, "\n", tidx2)
