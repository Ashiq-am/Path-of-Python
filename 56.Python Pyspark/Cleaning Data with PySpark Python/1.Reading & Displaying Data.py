# import necessary libraries
from pyspark.sql import SparkSession

# Create Spark Session
sparkSession = SparkSession.builder.appName('g1').getOrCreate()
