# importing row_number() from pyspark.sql.functions
from pyspark.sql.functions import row_number

# applying the row_number() function
df2.withColumn("row_number",
			row_number().over(windowPartition)).show()
