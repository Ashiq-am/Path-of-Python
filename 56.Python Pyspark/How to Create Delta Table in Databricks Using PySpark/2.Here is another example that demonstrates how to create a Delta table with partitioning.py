from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Delta Table Example").getOrCreate()

# Load the CSV file into a DataFrame
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Create a Delta table with partitioning
df.write.format("delta") \
   .option("path", "delta_table_partitioned") \
   .option("overwriteSchema", "true") \
   .partitionBy("age") \
   .save()
