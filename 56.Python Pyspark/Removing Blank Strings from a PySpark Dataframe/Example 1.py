# import the necessary libraries
from pyspark.sql import *
from pyspark.sql.functions import *

# create a SparkSession
spark = SparkSession.builder.appName('my_app').getOrCreate()

# create the dataframe
df = spark.createDataFrame([
	('John', 23, 'Male'),
	('', 25, 'Female'),
	('Jane', 28, 'Female'),
	('', 30, 'Male')
], ['Name', 'Age', 'Gender'])

# examine the database
df.show()
