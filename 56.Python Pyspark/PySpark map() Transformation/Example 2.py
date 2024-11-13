from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("\
map_example").getOrCreate()

# Create a DataFrame with sample data
data = [("Alice", 1),
		("Bob", 2), ("Charlie", 3)]
df = spark.createDataFrame(data,
						["name", "age"])

# Define a function to be applied to each row
def add_one(age):
	return age + 1

# Use the map() transformation to apply
# the function to the "age" column
df = df.rdd.map(lambda x: (x[0],
	add_one(x[1]))).toDF(["name", "age"])

# Show the resulting DataFrame
df.show()
