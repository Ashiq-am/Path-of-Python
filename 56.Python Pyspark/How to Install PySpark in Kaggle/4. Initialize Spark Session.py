from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
        .master("local") \
        .appName("MyApp") \
        .getOrCreate()

# Verify Spark Session
print(spark.version)
