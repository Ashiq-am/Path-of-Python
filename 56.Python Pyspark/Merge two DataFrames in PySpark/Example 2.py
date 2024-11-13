# import modules
from functools import reduce
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

# explicit functions
def unionAll(*dfs):
	return reduce(DataFrame.unionAll, dfs)


spark = SparkSession.builder.getOrCreate()

df1 = spark.createDataFrame([[1, 1], [2, 2]], ['a', 'b'])

# different column order.
df2 = spark.createDataFrame([[3, 333], [4, 444]], ['b', 'a'])
df3 = spark.createDataFrame([[555, 5], [666, 6]], ['b', 'a'])

unionAll(*[df1, df2, df3]).show()
