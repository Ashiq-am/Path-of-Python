# Create an empty list
Row_list =[]

# Iterate over each row
for i in range((df.shape[0])):

	# Using iloc to access the values of
	# the current row denoted by "i"
	Row_list.append(list(df.iloc[i, :]))

# Print the list
print(Row_list)
