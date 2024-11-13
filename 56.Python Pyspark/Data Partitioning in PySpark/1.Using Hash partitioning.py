# Import required modules
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("hash\
			_partitioning").getOrCreate()

# Create a sample DataFrame
df = spark.createDataFrame([
	(1, "Alice", 25),
	(2, "Bob", 30),
	(3, "Charlie", 35),
	(4, "Dave", 40),
	(5, "Eve", 45),
	(6, "Frank", 50)
], ["id", "name", "age"])

# Print the DataFrame
df.show()
# Perform hash partitioning on the
# DataFrame based on the "id" column
df = df.repartition(4, "id")

# Print the elements in each partition
print(df.rdd.glom().collect())
