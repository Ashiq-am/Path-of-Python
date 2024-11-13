from pyspark.sql import SparkSession
from pyspark.sql.types import *

# create a SparkSession
spark = SparkSession.builder.appName("SplitStructExample").getOrCreate()

# create a sample data
data = [("Alice", ("NYC", 10001)),
		("Bob", ("NYC", 10002))]

# define the schema of the DataFrame
schema = StructType([
	StructField("name", StringType()),
	StructField("address", StructType([
		StructField("city", StringType()),
		StructField("zip", IntegerType())
	]))
])

# create DataFrame using createDataFrame method
df = spark.createDataFrame(data, schema)
print("Data frame before splitting:")
df.show()

# Split struct column into separate columns
df2 = df.select("name", df["address.city"].alias("city"), df["address.zip"].alias("zip"))

# show the new DataFrame
print("Data frame after splitting:")
df2.show()
