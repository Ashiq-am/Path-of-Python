# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# Creating series data for address details w.r.t
# college names with same name with nested lists.
index_values = pd.Series([['sravan', 'address1', 'vignan'],
						['sravan', 'address2', 'vignan'],
						['sravan', 'address3', 'vignan'],
						['sravan', 'address4', 'vignan'],
						['vani', 'address5', 'vignan lara'],
						['vani', 'address6', 'vignan lara'],
						['vani', 'address7', 'vignan lara'],
						['vani', 'address8', 'vignan lara']])

# assinging values with integers
data = pd.Series(np.arange(1, 9),
				index=index_values)

# display data
print(data)

# mapping with data using '/' symbol with join
data1 = data.index.map('/'.join)

print(data1)
