# import the necessary libraries
from functools import reduce
from pyspark.sql import *
from pyspark.sql.functions import *

# create a SparkSession
spark = SparkSession.builder.appName('my_app').getOrCreate()

# create the dataframe
df = spark.createDataFrame([
	('John', 23, 'Male', '123 Main St.', '555-1234'),
	('', 25, 'Female', '456 Market St.', ''),
	('Jane', 28, 'Female', '789 Park Ave.', '555-9876'),
	('', 30, 'Male', '', '555-4321')
], ['Name', 'Age', 'Gender', 'Address', 'Phone'])

# examine the dataframe
df.show()
