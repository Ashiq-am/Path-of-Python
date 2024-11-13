from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Apply function to CSV").getOrCreate()

# Loading the csv file
df = spark.read.csv("sample.csv", header=True, inferSchema=True)
# Displaying the csv file
df.show()
