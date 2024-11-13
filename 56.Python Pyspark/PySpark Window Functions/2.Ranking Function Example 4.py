# importing dense_rank() from pyspark.sql.functions
from pyspark.sql.functions import dense_rank

# applying the dense_rank() function
df2.withColumn("dense_rank",
			dense_rank().over(windowPartition)).show()
