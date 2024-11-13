from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	'GeeksForGeeks').getOrCreate() # You can use any appName
print(spark)
