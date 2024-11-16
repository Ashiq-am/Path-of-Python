# importing pandas as pd
import pandas as pd

# Creating the MutiIndex
midx = pd.MultiIndex.from_arrays([['Mon', 'Tue', 'Wed', 'Thr'],
				[10, 20, 30, 40]], names =('Days', 'Target'))

# Print the MultiIndex
midx
