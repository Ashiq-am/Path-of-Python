# Importing required modules
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()

# Create a DataFrame
data = [("Alice", 25),
		("Bob", 30),
		("Charlie", 35)]

df = spark.createDataFrame(data,
						["name", "age"])
df.printSchema()

# Change column metadata
fields = [StructField(field.name,
		field.dataType,
		False) for field in df.schema.fields]

# Store changed data frame in new_schema
new_schema = StructType(fields)
df = spark.createDataFrame(df.rdd,
						new_schema)
df.printSchema()
