from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Create a DataFrame
df = spark.createDataFrame([(1, "Donald", 51),
							(2, "Riya", 23),
							(3, "Vani", 22)],
						["id", "name", "age"])

# Write dataframe to a JSON file
df.write.json('data.json')

# Merge JSON files into a single file
df.coalesce(1).write.json('data_merged.json')

# Printing data frame
df.show()
