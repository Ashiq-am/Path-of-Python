# Importing required modules
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import Row

# Create a SparkSession
spark = SparkSession.builder.appName("Myapp").getOrCreate()

# step 1: Define the schema for the dataframe
schema = StructType([
	StructField("name",
				StringType(), True),
	StructField("age",
				IntegerType(), True),
	StructField("salary",
				IntegerType(), True)
])

# step 2: Create a list of custom objects
data = [{"name": "John",
		"age": 30, "salary": 5000},
		{"name": "Mary",
		"age": 25, "salary": 6000},
		{"name": "Mike",
		"age": 35, "salary": 7000}]

# step 3: Create the dataframe
df = spark.createDataFrame(data, schema)

# step 4: Show the dataframe
df.show()
