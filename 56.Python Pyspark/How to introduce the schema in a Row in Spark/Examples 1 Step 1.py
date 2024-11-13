from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import Row

# Create a SparkSession object
spark = SparkSession.builder.appName("Schema").getOrCreate()
spark
