from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Delta Table Example").getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Create a Delta table
df.write.format("delta").save("delta_table")
