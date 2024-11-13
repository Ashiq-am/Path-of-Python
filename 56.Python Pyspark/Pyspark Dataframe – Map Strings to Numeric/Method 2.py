# import col and when modules
from pyspark.sql.functions import col, when

# map college name with colege number
# using with column method along with when module
dataframe.withColumn("college_number",
					when(col("college")=='iit', 1)
					.when(col("college")=='vignan', 2)
					.when(col("college")=='rvrjc', 3)
					.otherwise(4)).show()
