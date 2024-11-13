from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("JSON Creation").getOrCreate()

# Define the PySpark DataFrame schema with an array field
schema = StructType([
	StructField("name",
				StringType()),
	StructField("scores",
				ArrayType(IntegerType()))
])

# Create a PySpark DataFrame with an array field
data = [("Ali", [80, 90, 95]),
		("Bhim", [70, 85, 92])]
df = spark.createDataFrame(data, schema)

# Convert the PySpark DataFrame to a JSON string
json_string = df.toJSON().collect()[0]

print(json_string)

# Write the JSON string to a file
with open("example2.json", "w") as f:
	f.write(json_string)
