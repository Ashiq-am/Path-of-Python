# Importing PySpark and random
import pyspark
from pyspark.sql import SparkSession
import random

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

# Showing the DataFrame
df.show()

# Creating a list of rows and
# getting a random row from the list
row_list = df.collect()
repeated = random.choice(row_list)

# adding a row object to the list
# n times
for _ in range(n):

    row_list.append(repeated)

# Final DataFrame
df = Spark_Session.createDataFrame(row_list)

# Result
df.show()
