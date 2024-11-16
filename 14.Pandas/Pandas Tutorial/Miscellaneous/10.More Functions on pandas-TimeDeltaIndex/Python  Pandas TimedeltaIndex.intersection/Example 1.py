# importing pandas as pd
import pandas as pd

# Create the first TimedeltaIndex object
tidx1 = pd.TimedeltaIndex(start ='11 days 22:11:12.001124', periods = 5,
										freq ='T', name ='New_object')

# Create the seccond TimedeltaIndex object
tidx2 = pd.TimedeltaIndex(start ='11 days 22:14:12.001124', periods = 5,
										freq ='T', name ='New_object')

# Print the first and second TimedeltaIndex object
print(tidx1, '\n', tidx2)
