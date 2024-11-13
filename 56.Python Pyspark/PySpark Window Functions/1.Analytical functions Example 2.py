# importing lag() from pyspark.sql.functions
from pyspark.sql.functions import lag

df.withColumn("Lag", lag("Salary", 2).over(windowPartition)) \
	.show()
