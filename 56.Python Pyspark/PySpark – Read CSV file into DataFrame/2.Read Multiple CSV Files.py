from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Read Multiple CSV Files').getOrCreate()

path = ['/content/authors.csv',
		'/content/book_author.csv']

files = spark.read.csv(path, sep=',',
					inferSchema=True, header=True)

df1 = files.toPandas()
display(df1.head())
display(df1.tail())
