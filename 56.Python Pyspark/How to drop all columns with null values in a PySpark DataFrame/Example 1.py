import pyspark.sql.functions as sqlf
from pyspark.sql import SparkSession
import findspark

findspark.init()


spark: SparkSession = SparkSession.builder \
	.master("local[1]") \
	.appName("SparkByExamples.com") \
	.getOrCreate()

filePath = "example1.csv"
df = spark.read.options(header='true', inferSchema='true') \
		.csv(filePath)

df.printSchema()
df.show(truncate=False)
