# import the necessary libraries
from pyspark.sql import *
from pyspark.sql.functions import *

# create a SparkSession
spark = SparkSession.builder.appName('my_app').getOrCreate()

# create the dataframe
df = spark.createDataFrame([
	('John', 23, 'Male', '123 Main St.'),
	('', 25, 'Female', '456 Market St.'),
	('Jane', 28, 'Female', '789 Park Ave.'),
	('', 30, 'Male', '')
], ['Name', 'Age', 'Gender', 'Address'])

# examine the dataframe
df.show()
