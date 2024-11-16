# importing pandas and numpy libraries
import numpy as np
import pandas as pd

# generating 7 random integers from 5 to 35
data = np.random.randint(5, 35, size = 7)
df = pd.DataFrame(data, columns = ['integers'])

# displaying random integers in data frame
print("Before Sorting :")
print(df)

# sorting the random integer values
# using dataframe.sort_values()
# and displaying them
df.sort_values("integers", axis = 0, ascending = True,
				inplace = True, na_position ='last')

print("After Sorting :")
print(df)
