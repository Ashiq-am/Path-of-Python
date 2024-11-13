# pyspark program to demonstrate the MapType
# Import the neccessary modules.
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import MapType, StringType, IntegerType

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Define the key and value data types for the map
key_type = StringType()
value_type = IntegerType()

# Create the MapType
map_type = MapType(key_type, value_type)

# Sample data
data = [
	(1, {"apple": 3, "orange": 2}),
	(2, {"banana": 4, "kiwi": 1}),
	(3, {"grape": 5, "mango": 2})
]

# Create a DataFrame
df = spark.createDataFrame(data, ["id", "fruit_counts"])

# Define the schema with MapType
schema = df.schema
schema["fruit_counts"].dataType = map_type

# Apply the modified schema to the DataFrame
df = spark.createDataFrame(df.rdd, schema)

# Print the DataFrame
df.show(truncate=False)
