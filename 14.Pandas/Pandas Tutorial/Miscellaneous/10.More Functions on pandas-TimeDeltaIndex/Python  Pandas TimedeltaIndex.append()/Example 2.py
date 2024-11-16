# importing pandas as pd
import pandas as pd

# Create the first TimedeltaIndex object
tidx1 = pd.TimedeltaIndex(start ='1 days 02:00:12.001124', periods = 5,
											freq ='N', name ='Koala')

# Create the second TimedeltaIndex object
tidx2 = pd.TimedeltaIndex(data =['-1 days 2 min 3us 10ns',
								'1 days 06:05:01.000030',
								'-1 days + 23:59:59.999999'])

# Create the third TimedeltaIndex object
tidx3 = pd.TimedeltaIndex(data =['-3 days 02:10:00',
								'1 days 06:05:01.000030',
								'1 days 02:00:00'], name ='MyObjejct')

# Print the first TimedeltaIndex object
print(tidx1)

# Print the second TimedeltaIndex object
print(tidx2)

# Print the third TimedeltaIndex object
print(tidx3)
