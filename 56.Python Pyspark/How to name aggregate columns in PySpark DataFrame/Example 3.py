# importing count function
from pyspark.sql.functions import count

# group the salary among different
# sectors and name as Total-People
# by count aggregation
dataframe.groupBy("sector").agg(count("salary").alias("Total-People")).show()
