from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	'Read CSV File into DataFrame').getOrCreate()

authors = spark.read.csv('/content/authors.csv', sep=',',
						inferSchema=True, header=True)

df = authors.toPandas()
df.head()
