# Starting the Spark Session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('LinearRegression').getOrCreate()
spark
