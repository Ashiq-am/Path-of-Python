# Define the number of splits you want
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import concat, col, lit

n_splits = 4

# Calculate count of each dataframe rows
each_len = prod_df.count() // n_splits

# Create a copy of original dataframe
copy_df = prod_df

# Function to modify columns of each individual split


def modify_dataframe(data):
	return data.select(
		concat(col("Brand"), lit(" - "),
			col("Product"))
	)


# Create an empty dataframe to
# store concatenated results
schema = StructType([
	StructField('Brand - Product', StringType(), True)
])
result_df = spark.createDataFrame(data=[],
								schema=schema)

# Iterate for each dataframe
i = 0
while i < n_splits:

	# Get the top `each_len` number of rows
	temp_df = copy_df.limit(each_len)

	# Truncate the `copy_df` to remove
	# the contents fetched for `temp_df`
	copy_df = copy_df.subtract(temp_df)

	# Perform operation on the newly created dataframe
	temp_df_mod = modify_dataframe(data=temp_df)
	temp_df_mod.show(truncate=False)

	# Concat the dataframe
	result_df = result_df.union(temp_df_mod)

	# Increment the split number
	i += 1

result_df.show(truncate=False)
