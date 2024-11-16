# importing pandas module
import pandas as pd

# Creating series data for address details
index_values = pd.Series([('sravan', 'address1'),
						('sravan', 'address2'),
						('sudheer', 'address1'),
						('sudheer', 'address2')])

# assinging values with integers
data = pd.Series(np.arange(1, 5), index=index_values)

# display data
print(data)

# mapping with data using '_' symbol with join
data1 = data.index.map('_'.join)

print(data1)
