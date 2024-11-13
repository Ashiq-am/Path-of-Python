# importing avg function
from pyspark.sql.functions import avg

# group the salary among different sectors
# and name as Average_Employee_salary
# by average aggregation
dataframe.groupBy("sector").agg(avg("salary").alias("Average_Employee_salary")).show()
