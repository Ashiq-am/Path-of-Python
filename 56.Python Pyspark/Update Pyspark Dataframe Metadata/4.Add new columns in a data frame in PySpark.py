# Import required modules
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
data = [("Alice", 25),
		("Bob", 30),
		("Charlie", 35)]
df = spark.createDataFrame(data,
						["name", "age"])
df.printSchema()

# Add column
from pyspark.sql.functions import lit
df = df.withColumn("gender",
				lit("unknown"))

# Print Schema of data frame
df.printSchema()
df.show()
