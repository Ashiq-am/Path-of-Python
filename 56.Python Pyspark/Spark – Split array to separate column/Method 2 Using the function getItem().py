# importing packages
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, col

# creating a spark session
spark = SparkSession.builder.appName('split_array_to_columns').getOrCreate()


data = [(1, ['apple', 'banana', 'orange']),
		(2, ['grape', 'kiwi', 'pineapple', 'watermelon']),
		(3, ['peach', 'pear'])]
# creating a dataframe
df = spark.createDataFrame(data, ['id', 'fruits'])
df.show()

# splitting the fruits column into multiple columns
df = df.select('id',* [col('fruits').getItem(i).alias(fruit(i+1))
for i in range(0, 4)])
df.printSchema()
