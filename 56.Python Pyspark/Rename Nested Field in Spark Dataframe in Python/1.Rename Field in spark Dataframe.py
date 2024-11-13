from pyspark.sql import SparkSession
# Create a SparkSession
spark = SparkSession.builder.appName ("CreateDF").getOrCreate()
data = [(1, "John", "a", 25), (2, "Mike",
			"b", 30), (3, "Sara", "c", 35)]

# Create a DataFrame
df = spark.createDataFrame(data,
			["id", "fname", "lname", "age"])
df.printSchema()
