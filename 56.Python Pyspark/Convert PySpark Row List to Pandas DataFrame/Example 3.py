# Importing PySpark
# Importing Pandas for append()
import pyspark
import pandas
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

# Our final DataFrame initialized
mega_df = pandas.DataFrame()

# Traversing through the list
for i in range(len(row_object_list)):

	# Creating a Spark DataFrame of a single row
	small_df = row_pandas_session.createDataFrame([row_object_list[i]])

	# appending the Pandas version of small_df
	# to mega_df
	mega_df = mega_df.append(small_df.toPandas(),
							ignore_index=True)

# Printing our desired DataFrame
print(mega_df)
