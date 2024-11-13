# Declare an empty Dictionary
dict = {}

# Convert PySpark DataFrame to Pandas
# DataFrame
df = df.toPandas()

# Traverse through each column
for column in df.columns:

	# Add key as column_name and
	# value as list of column values
	dict[column] = df[column].values.tolist()

# Print the dictionary
print(dict)
