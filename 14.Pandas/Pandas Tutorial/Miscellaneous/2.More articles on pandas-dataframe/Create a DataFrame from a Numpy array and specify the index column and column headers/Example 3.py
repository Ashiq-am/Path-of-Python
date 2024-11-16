# importiong the modules
import pandas as pd
import numpy as np

# creating the Numpy array
array = np.array([['CEO', 20, 5], ['CTO', 22, 4.5],
				['CFO', 21, 3], ['CMO', 24, 2]])

# creating a list of index names
index_values = [1, 2, 3, 4]

# creating a list of column names
column_values = ['Names', 'Age',
				'Net worth in Millions']

# creating the dataframe
df = pd.DataFrame(data = array,
				index = index_values,
				columns = column_values)

# displaying the dataframe
print(df)
