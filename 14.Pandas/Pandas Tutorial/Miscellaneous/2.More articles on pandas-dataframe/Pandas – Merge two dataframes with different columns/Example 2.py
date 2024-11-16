# Import pandas library
import pandas as pd

# initialize list of lists
data = [['sravan', 98.00], ['jyothika', 90.00], ['vijay', 79.34]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Marks'])

# print dataframe.
df
