# importing percent_rank() from pyspark.sql.functions
from pyspark.sql.functions import percent_rank

# applying the percent_rank() function
df2.withColumn("percent_rank",
			percent_rank().over(windowPartition)).show()
