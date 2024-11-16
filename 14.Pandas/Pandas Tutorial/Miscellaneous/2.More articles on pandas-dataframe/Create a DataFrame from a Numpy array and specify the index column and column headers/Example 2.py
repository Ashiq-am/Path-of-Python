# importiong the modules
import pandas as pd
import numpy as np

# creating the Numpy array
array = np.array([['Aditya', 20], ['Samruddhi', 15],
				['Rohan', 21], ['Anantha', 20],
				['Abhinandan', 21]])

# creating a list of index names
index_values = ['A', 'B', 'C', 'D', 'E']

# creating a list of column names
column_values = ['Names', 'Age']

# creating the dataframe
df = pd.DataFrame(data = array,
				index = index_values,
				columns = column_values)

# displaying the dataframe
print(df)
