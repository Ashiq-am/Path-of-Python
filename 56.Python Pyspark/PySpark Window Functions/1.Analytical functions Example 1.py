# importing cume_dist()
# from pyspark.sql.functions
from pyspark.sql.functions import cume_dist

# applying window function with
# the help of DataFrame.withColumn
df.withColumn("cume_dist",
			cume_dist().over(windowPartition)).show()
