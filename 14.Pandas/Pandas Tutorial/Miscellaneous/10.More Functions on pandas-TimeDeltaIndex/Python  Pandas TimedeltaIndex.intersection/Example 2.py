# importing pandas as pd
import pandas as pd

# Create the first TimedeltaIndex object
tidx1 = pd.TimedeltaIndex(start ='1 days 02:00:12.001124',periods = 5, freq ='D', name ='Koala')

# Create the second TimedeltaIndex object
tidx2 = pd.TimedeltaIndex(start ='3 days 02:00:12.001124',periods = 5, freq ='D', name ='Koala')

# Print the first and second TimedeltaIndex object
print(tidx1, '\n', tidx2)
