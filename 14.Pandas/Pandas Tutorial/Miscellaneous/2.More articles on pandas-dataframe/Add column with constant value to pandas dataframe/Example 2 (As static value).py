# import packages
import pandas as pd
import numpy as np

# create dataframe
df = pd.DataFrame({'Name': {0: 'Ram', 1: 'Deep', 2: 'Yash', 3: 'Aman', 4: 'Akash'},
				'Marks': {0: 68, 1: 87, 2: 45, 3: 78, 4: 56}})


# view dataframe
print("Initial dataframe")
display(df)


# adding column with constant value
df['Pass'] = True

# view dataframe
print("Final dataframe")
display(df)
