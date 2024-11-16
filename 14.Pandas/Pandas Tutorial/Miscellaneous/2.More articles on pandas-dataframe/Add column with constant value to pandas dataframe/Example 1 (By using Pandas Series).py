# import packages
import pandas as pd
import numpy as np

# create dataframe
df = pd.DataFrame({'Number': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5},
				'Power 2': {0: 1, 1: 4, 2: 9, 3: 16, 4: 25},
				'Power 3': {0: 1, 1: 8, 2: 27, 3: 64, 4: 125}})

# view dataframe
print("Initial dataframe")
display(df)


# adding column with constant value
df['Power 0'] = pd.Series([1 for x in range(len(df.index))])

# view dataframe
print("Final dataframe")
display(df)
