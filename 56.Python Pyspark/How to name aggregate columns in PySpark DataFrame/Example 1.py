# importing sum function
from pyspark.sql.functions import sum

# group the salary among different sectors
# and name as Employee_salary by sum aggregation
dataframe.groupBy("sector").agg(sum("salary").alias("Employee_salary")).show()
