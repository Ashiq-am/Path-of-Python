# Define the number of splits you want
n_splits = 4

# Calculate count of each dataframe rows
each_len = prod_df.count() // n_splits

# Create a copy of original dataframe
copy_df = prod_df

# Iterate for each dataframe
i = 0
while i < n_splits:

	# Get the top `each_len` number of rows
	temp_df = copy_df.limit(each_len)

	# Truncate the `copy_df` to remove
	# the contents fetched for `temp_df`
	copy_df = copy_df.subtract(temp_df)

	# View the dataframe
	temp_df.show(truncate=False)

	# Increment the split number
	i += 1
