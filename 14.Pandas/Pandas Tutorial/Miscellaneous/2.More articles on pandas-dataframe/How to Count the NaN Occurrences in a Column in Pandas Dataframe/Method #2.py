# importing necessary packages
import pandas as pd
import numpy as np

# creating data
data = [[1, "M", np.nan], [5, "A", 3.2],
		[np.nan, np.nan, 4.6], [1, "D", np.nan]]

# converting data to data frame
data_frame = pd.DataFrame(data, columns=["col1", "col2", "col3"])

# printing original data frame
print("\nOriginal Data Frame:")
print(data_frame)

# counting NaN values of col1
length = len(data_frame)
count_in_col3 = data_frame['col3'].count()
cnt = length - count_in_col3

# printing count of NaN values
print("\nNan in col3:", cnt)
