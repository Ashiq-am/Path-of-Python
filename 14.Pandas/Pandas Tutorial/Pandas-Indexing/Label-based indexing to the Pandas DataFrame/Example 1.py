# importing pandas library
import pandas as pd

# Creating a Data frame
df = pd.DataFrame([['1993', 'x', 5, 4, 7, 2],
				['1994', 'v', 10, 1, 2, 0],
				['1995', 'z', 2, 1, 4, 12],
				['1996', 'y', 2, 1, 10, 1],
				['1998', 'x', 2, 10, 40, 12],
				['1999', 'x', 5, 8, 11, 6]],
				columns=('Year', 'Alpha', 'x', 'y', 'z', 'v'))

# Display Data frame
df
