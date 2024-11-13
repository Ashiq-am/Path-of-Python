# Importing SparkSession
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Create a DataFrame
df = spark.createDataFrame([(1, "Joseph", 10),
							(2, "Jack", 20),
							(3, "Elon", 30)],
							["id", "name", "age"])

print("Dataframe: ")
df.show()

# Convert dataframe to a Pandas dataframe
pandas_df = df.toPandas()

# Convert Pandas dataframe to a JSON string
json_data = pandas_df.to_json(orient='records')

# Print the JSON array
print("JSON array:", json_data)
