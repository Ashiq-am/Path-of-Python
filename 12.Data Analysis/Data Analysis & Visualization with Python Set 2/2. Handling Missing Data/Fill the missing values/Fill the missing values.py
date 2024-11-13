import numpy as np
import pandas as pd

# Create a DataFrame
dframe = pd.DataFrame({'Geeks': [23, 24, 22],
						'For': [10, 12, np.nan],
						'geeks': [0, np.nan, np.nan]},
						columns = ['Geeks', 'For', 'geeks'])

# Use fillna of complete Dataframe

# value function will be applied on every column
dframe.fillna(value = dframe.mean(), inplace = True)
print(dframe)

# filling value of one column
dframe['For'].fillna(value = dframe['For'].mean(),
									inplace = True)
print(dframe)
