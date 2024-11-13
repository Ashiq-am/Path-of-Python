# pyspark code to demonstrate explode on maptype
# Import neccessary modules and functions.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

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

# Explode the MapType column
exploded_df = df.select("id", explode("fruit_counts").alias("fruit", "count"))

# Print the exploded DataFrame
exploded_df.show(truncate=False)
