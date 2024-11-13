# Import necessary libraries
from pyspark.sql.functions import col

# Create a sample DataFrame
data = [(1, 2), (3, 4), (5, 6)]
df = spark.createDataFrame(data, ["col1", "col2"])

# Define a function to add two columns
def add_columns(row):
	return (row[0], row[1], row[0] + row[1])

# Apply the function to each row of the DataFrame
new_rdd = df.rdd.map(add_columns)

# Convert the RDD back to a DataFrame
new_df = new_rdd.toDF(["col1", "col2", "sum"])

# Display the results
new_df.show()
