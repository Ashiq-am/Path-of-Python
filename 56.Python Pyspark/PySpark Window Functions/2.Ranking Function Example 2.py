# importing rank() from pyspark.sql.functions
from pyspark.sql.functions import rank

# applying the rank() function
df2.withColumn("rank", rank().over(windowPartition)) \
	.show()
