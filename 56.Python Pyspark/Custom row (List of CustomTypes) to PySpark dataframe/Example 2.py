from pyspark.sql import Row
from pyspark.sql import SparkSession
# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()
# Define a custom class to represent a row in the dataframe
class CustomType:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

# Create a list of CustomType objects
data = [CustomType("John", 30, 5000),
		CustomType("Mary", 25, 6000),
		CustomType("Mike", 35, 7000)]

rdd = spark.sparkContext.parallelize(data)

# Create a dataframe from the rdd
df = spark.createDataFrame(rdd)

# Show the dataframe
df.show()
