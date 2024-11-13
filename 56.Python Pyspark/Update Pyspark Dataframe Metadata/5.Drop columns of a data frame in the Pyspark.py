# Importing required modules
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()

# Create a DataFrame
schema = StructType([
	StructField("name", StringType()),
	StructField("age", IntegerType())
])

# Create a DataFrame
data = [("Alice", 25, "female"),
		("Bob", 30, "male"),
		("Charlie", 35, "male")]
df = spark.createDataFrame(data,
						["name",
							"age",
							"gender"])
df.printSchema()

# Remove column
df = df.drop("gender")
df.printSchema()
