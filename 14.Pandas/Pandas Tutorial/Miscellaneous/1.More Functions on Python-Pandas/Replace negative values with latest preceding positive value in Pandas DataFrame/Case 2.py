import pandas as pd

# creating a pandas dataframe
data_frame = pd.DataFrame({'col1': [8, -2, 0, 3, 51, 2],
						'col2': [-1, -2, -5, -7, 0, -1],
						'col3': [-1, -12, -5, 4, 5, 3]})

print("Original DataFrame")
print(data_frame)

# masking the data frame
data_frame = data_frame.mask(data_frame.lt(
	0)).ffill().fillna(0).astype('int32')

print("Modified DataFrame")
print(data_frame)
