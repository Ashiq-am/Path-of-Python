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

# Change column names
from pyspark.sql.types import DoubleType
df = df.withColumn("age",
				df["age"].cast(DoubleType()))

df.printSchema()
