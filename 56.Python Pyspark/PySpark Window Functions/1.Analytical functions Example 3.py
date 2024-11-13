# importing lead() from pyspark.sql.functions
from pyspark.sql.functions import lead

df.withColumn("Lead", lead("salary", 2).over(windowPartition)) \
	.show()
