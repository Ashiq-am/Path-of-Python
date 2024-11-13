# Importing PySpark and importantly
# Row from pyspark.sql
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

# PySpark Session
row_pandas_session = SparkSession.builder.appName(
	'row_pandas_session'
).getOrCreate()

# List of Sample Row objects
row_object_list = [Row(Topic='Dynamic Programming', Difficulty=10),
				Row(Topic='Arrays', Difficulty=5),
				Row(Topic='Sorting', Difficulty=6),
				Row(Topic='Binary Search', Difficulty=7)]

# Creating an RDD
rdd = row_pandas_session.sparkContext.parallelize(row_object_list)

# DataFrame created using RDD
df = row_pandas_session.createDataFrame(rdd)

# Checking the DataFrame
df.show()

# Conversion of DataFrame
df2 = df.toPandas()

# Final DataFrame needed
print(df2)
