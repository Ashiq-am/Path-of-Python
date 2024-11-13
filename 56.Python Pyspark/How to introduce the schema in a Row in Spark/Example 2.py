from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import Row

# Create a SparkSession object
spark = SparkSession.builder.appName("example").getOrCreate()

# Define the schema
schema = StructType([
	StructField("id", IntegerType(), True),
	StructField("name", StringType(), True),
	StructField("age", IntegerType(), True)
])

# Create a Row object
row = Row(id=100, name="Akshat", age=19)

# Create a DataFrame from the Row object and the schema
df = spark.createDataFrame([row], schema=schema)

# Show the DataFrame
df.show()

# print the schema
df.printSchema()

# Stop the SparkSession
spark.stop()
