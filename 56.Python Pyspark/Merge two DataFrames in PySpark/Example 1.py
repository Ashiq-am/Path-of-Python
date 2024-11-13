# import modules
from pyspark.sql import SparkSession
import functools

# explicit function
def unionAll(dfs):
	return functools.reduce(lambda df1, df2: df1.union(df2.select(df1.columns)), dfs)


spark = SparkSession.builder.getOrCreate()
df1 = spark.createDataFrame([[1, 1], [2, 2]], ['a', 'b'])

# different column order.
df2 = spark.createDataFrame([[3, 333], [4, 444]], ['b', 'a'])
df3 = spark.createDataFrame([[555, 5], [666, 6]], ['b', 'a'])

unioned_df = unionAll([df1, df2, df3])
unioned_df.show()
