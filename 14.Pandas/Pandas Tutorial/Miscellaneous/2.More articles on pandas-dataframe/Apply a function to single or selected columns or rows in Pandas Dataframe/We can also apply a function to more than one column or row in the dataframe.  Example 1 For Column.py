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

# Apply function numpy.square()
# for square the values of
# two columns 'x' and 'y'
new_df = df.apply(lambda x: np.square(x) if x.name in ['x', 'y'] else x)

# Output
new_df
