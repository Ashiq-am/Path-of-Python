# Importing required modules
from pyspark.sql import Row
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
# Define a custom class to represent a row in the dataframe
class CustomType:
	def __init__(self, name,
				age, salary):
		self.name = name
		self.age = age
		self.salary = salary

# Create a list of CustomType objects
data = [CustomType("John", 30, 5000),
		CustomType("Mary", 25, 6000),
		CustomType("Mike", 35, 7000)]

# Convert the list of CustomType
# objects to a list of Row objects
rows = [Row(name=d.name,
			age=d.age,
			salary=d.salary) for d in data]

# Create a dataframe from the list of Row objects
df = spark.createDataFrame(rows)

# Show the dataframe
df.show()
