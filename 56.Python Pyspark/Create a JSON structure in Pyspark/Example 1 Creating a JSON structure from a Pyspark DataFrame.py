from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("JSON Creation").getOrCreate()

# Define the PySpark DataFrame schema
schema = StructType([
	StructField("name", StringType()),
	StructField("age", IntegerType()),
	StructField("city", StringType())
])

# Create a PySpark DataFrame
data = [("Shyam", 25, "New York"),
		("Ram", 30, "San Francisco")]
df = spark.createDataFrame(data, schema)

# Convert the PySpark DataFrame to a JSON string
json_string = df.toJSON().collect()[0]

print(json_string)

# Write the JSON string to file
with open("example1.json", "w") as f:
	f.write(json_string)
