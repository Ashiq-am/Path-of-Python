import numpy as np

# Convert the dataframe into list
# of rows
rows = [list(row) for row in df.collect()]

# COnvert the list into numpy array
ar = np.array(rows)

# Declare an empty dictionary
dict = {}

# Get through each column
for i, column in enumerate(df.columns):

	# Add ith column as values in dict
	# with key as ith column_name
	dict[column] = list(ar[:, i])

# Print the dictionary
print(dict)
