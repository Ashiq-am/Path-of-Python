# import module
import pandas as pd

# assign dataframes
data1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
					columns=['A', 'B', 'C'])

data2 = pd.DataFrame([[3, 4], [5, 6]],
					columns=['A', 'C'])

# display dataframes
print('Dataframes:')
display(data1)
display(data2)

# merge two data frames
print('After merging:')
pd.concat([data1, data2], axis=0)
