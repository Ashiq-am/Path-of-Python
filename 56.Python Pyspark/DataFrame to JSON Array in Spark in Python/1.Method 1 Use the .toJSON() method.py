# Importing SparkSession
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Create a DataFrame
df = spark.createDataFrame([(1, "Alice", 10),
							(2, "Bob", 20),
							(3, "Charlie", 30)],
						["id", "name", "age"])

print("Dataframe: ")
df.show()

# Convert the DataFrame to a JSON array
json_array = df.toJSON().collect()

# Print the JSON array
print("JSON array:",json_array)
