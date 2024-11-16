# importing pandas and numpy libraries
import numpy as np
import pandas as pd

# generating 6x2 i.e 12 random integers
# from 5 to 40
data = np.random.randint(5, 40, size = (6, 2))
df = pd.DataFrame(data, columns = ['random_col_1', 'random_col_2'])

# displaying random integers in data frame
print("Before Sorting :")
print(df)

# Sorting both Random integer column
# First column 1 is sorted
# then for every column 1, column 2 is sorted
# in ascending order
# using dataframe.sort_values()
df.sort_values(['random_col_1', 'random_col_2'], axis = 0,
			ascending = [True, True], inplace = True)

print("After Sorting :")
print(df)
