from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
	'Read All CSV Files in Directory').getOrCreate()

f2 = spark.read.csv('/content/*.csv', sep=',',
					inferSchema=True, header=True)

df1 = file2.toPandas()
display(df1.head())
display(df1.tail())
