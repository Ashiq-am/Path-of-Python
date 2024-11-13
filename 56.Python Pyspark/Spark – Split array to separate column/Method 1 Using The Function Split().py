# importing packages
from pyspark.sql.functions import split
from pyspark.sql import SparkSession

# creating a spark session
spark = SparkSession.builder.appName('split_array_to_columns').getOrCreate()

# Create a PySpark DataFrame
df = spark.createDataFrame([(1, "apple,orange,banana"),
							(2, "grape,kiwi,peach")], ["id", "fruits"])

# Split the "fruits" column into an array of strings
df = df.withColumn("fruit_list", split(df.fruits, ","))

# Show the resulting DataFrame
df.show()

df3 = df.select(
	df.fruit_list.getItem(0).alias('fruit1'),
	df.fruit_list.getItem(1).alias('fruit2'),
	df.fruit_list.getItem(2).alias('fruit3')
)

df3.show()
