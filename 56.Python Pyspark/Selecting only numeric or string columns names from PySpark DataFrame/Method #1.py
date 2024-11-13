from pyspark.sql import Row
from datetime import date
from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

# Creating dataframe from list of Row
df = spark.createDataFrame([
	Row(a=1, b='string1', c=date(2021, 1, 1)),
	Row(a=2, b='string2', c=date(2021, 2, 1)),
	Row(a=4, b='string3', c=date(2021, 3, 1))
])

# Printing DataFrame structure
print("DataFrame structure:", df)

# Getting list of columns and printing
# result
dt = df.dtypes
print("dtypes result:", dt)

# Getting list of columns having type
# string or bigint
# This statement will loop over all the
# tuples present in dt list
# item[0] will contain column name and
# item[1] will contain column type
columnList = [item[0] for item in dt if item[1].startswith(
	'string') or item[1].startswith('bigint')]
print("Result: ", columnList)
