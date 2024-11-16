# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(start ='1 days 02:00:00', periods = 5,
									freq ='T', name ='Koala')

# Print the TimedeltaIndex
print(tidx)
