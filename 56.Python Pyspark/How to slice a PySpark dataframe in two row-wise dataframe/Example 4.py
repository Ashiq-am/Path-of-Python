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

# DataFrame is created
df = Spark_Session.createDataFrame(rows, columns)

# Converting DataFrame to pandas
pandas_df = df.toPandas()

# First DataFrame formed by slicing
df1 = pandas_df.iloc[:2]

# Second DataFrame formed by slicing
df2 = pandas_df.iloc[2:]

# Converting the slices to PySpark DataFrames
df1 = Spark_Session.createDataFrame(df1)
df2 = Spark_Session.createDataFrame(df2)

# Printing the first slice
print('First DataFrame')
df1.show()

# Printing the second slice
print('Second DataFrame')
df2.show()
