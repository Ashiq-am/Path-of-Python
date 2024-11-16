# porgam to depict deep copy
# in pandas dataframe

# import module
import pandas as pd

# assign dataframe
df = pd.DataFrame({'index': [1, 2, 3, 4],
				'GFG': ['Mandy', 'Ron', 'Jacob', 'Bayek']})

# deep copy
copydf = df.copy(deep=True)

# comparing shallow copied datframe
# and original dataframe
print('\nBefore Operation:\n', copydf == df)

# assignmnet operation
copydf['index'] = [0, 0, 0, 0]


# comparing shallow copied datframe
# and original dataframe
print('\nAfter Operation:\n', copydf == df)

print('\nOriginal Dataframe after operation:\n', df)
