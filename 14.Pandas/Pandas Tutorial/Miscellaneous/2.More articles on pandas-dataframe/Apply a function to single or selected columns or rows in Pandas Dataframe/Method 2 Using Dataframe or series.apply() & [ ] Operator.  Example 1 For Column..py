# import pandas and numpy library
import pandas as pd
import numpy as np

# List of Tuples
matrix = [(1, 2, 3),
		(4, 5, 6),
		(7, 8, 9)
		]

# Create a DataFrame object
df = pd.DataFrame(matrix, columns = list('xyz'),
				index = list('abc'))

# Apply a function to one column 'z'
# and assign it back to the same column
df['z'] = df['z'].apply(np.square)

# Output
df
