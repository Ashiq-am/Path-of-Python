# import packages
import numpy as np
import pandas as pd

# setting a seed
np.random.seed(123)
# creating a dataframe
df = pd.DataFrame({'TeamA': np.random.randint(30, 100, 10),
				'TeamB': np.random.randint(30, 100, 10),
				'TeamC': np.random.randint(30, 100, 10)})
print('Before assigning the new column')

print(df)
# using assign() method to add a new column
scores = np.random.randint(30, 100, 10)

df2 = df.assign(TeamD=scores)

print('After assigning the new column')

print(df2)
