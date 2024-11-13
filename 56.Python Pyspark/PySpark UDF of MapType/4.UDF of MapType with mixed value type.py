from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import MapType, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [
	(1, {"apple": 3, "orange": "two"}),
	(2, {"banana": "four", "kiwi": 1}),
	(3, {"grape": 5, "mango": "three"})
]

# Create a DataFrame
df = spark.createDataFrame(data, ["id", "fruit_counts"])

# Define a UDF to process map values
def process_map(map_value):
	processed_map = {}
	for key, value in map_value.items():
		if isinstance(value, str):
			processed_map[key] = value.upper()
		elif isinstance(value, int):
			processed_map[key] = value * 2
		else:
			processed_map[key] = None
	return processed_map

# Register the UDF
process_map_udf = udf(process_map, MapType(StringType(), StringType()))

# Apply the UDF to the map column
processed_df = df.withColumn("processed_counts", process_map_udf(col("fruit_counts")))

# Print the DataFrame
processed_df.show(truncate=False)
