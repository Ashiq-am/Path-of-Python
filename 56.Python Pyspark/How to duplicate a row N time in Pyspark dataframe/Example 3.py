# Importing PySpark and Pandas
import pyspark
from pyspark.sql import SparkSession
import pandas as pd

# Session Creation
Spark_Session = SparkSession.builder.appName(
	'Spark Session'
).getOrCreate()

# Accepting n from the user.
n = int(input('Enter n : '))

# Data filled in our DataFrame
rows = [['a',1,'@'],
		['b',3,'_'],
		['c',2,'!'],
		['d',6,'(']]

# Columns of our DataFrame
columns = ['X','Y','Z']

# DataFrame is created
df = Spark_Session.createDataFrame(rows,columns)

# Converting to a Pandas DataFrame
df_pandas = df.toPandas()

# The initial DataFrame
print('First DF')
print(df_pandas)

# the first row
first_row = df_pandas[:1]

# Appending the row n times
for _ in range(n):
df_pandas = df_pandas.append(first_row,ignore_index = True)

# Final DataFrame
print('New DF')
print(df_pandas)
