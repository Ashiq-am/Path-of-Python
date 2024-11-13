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

# creating PySpark DataFrame using createDataFrame()
df = row_pandas_session.createDataFrame(row_object_list)

# Printing the Spark DataFrame
df.show()

# Conversion to Pandas DataFrame
pandas_df = df.toPandas()

# Final Result
print(pandas_df)
