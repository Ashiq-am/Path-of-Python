# Importing PySpark and Pandas
import pyspark
from pyspark.sql import SparkSession
import pandas as pd

# Session Creation
Spark_Session = SparkSession.builder.appName(
	'Spark Session'
).getOrCreate()


# Data filled in our DataFrame
rows = [['Lee Chong Wei', 69, 'Malaysia'],
		['Lin Dan', 66, 'China'],
		['Srikanth Kidambi', 9, 'India'],
		['Kento Momota', 15, 'Japan']]

# Columns of our DataFrame
columns = ['Player', 'Titles', 'Country']

#DataFrame is created
df = Spark_Session.createDataFrame(rows, columns)

# getting the list of Row objects
row_list = df.collect()

# Slicing the Python List
part1 = row_list[:1]
part2 = row_list[1:]

# Converting the slices to PySpark DataFrames
slice1 = Spark_Session.createDataFrame(part1)
slice2 = Spark_Session.createDataFrame(part2)

# Printing the first slice
print('First DataFrame')
slice1.show()

# Printing the second slice
print('Second DataFrame')
slice2.show()
