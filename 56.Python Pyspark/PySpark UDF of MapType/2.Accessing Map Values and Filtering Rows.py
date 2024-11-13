# pyspark program to demonstrate accessing elements and filtering in MapType.
# Import neccessary module and functions.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
	(1, {"apple": 3, "orange": 2}),
	(2, {"banana": 4, "kiwi": 1}),
	(3, {"grape": 5, "mango": 2})
]

# Create a DataFrame
df = spark.createDataFrame(data, ["id", "fruit_counts"])

# Access map values using getItem()
df = df.withColumn("apple_count", col("fruit_counts").getItem("apple"))

# Filter rows based on a condition
filtered_df = df.filter(col("apple_count") > 2)

# Print the filtered DataFrame
filtered_df.show(truncate=False)
