# importing window from pyspark.sql.window
from pyspark.sql.window import Window

# importing aggregate functions
# from pyspark.sql.functions
from pyspark.sql.functions import col,avg,sum,min,max,row_number

# creating a window partion of dataframe
windowPartitionAgg = Window.partitionBy("Department")

# applying window aggregate function
# to df3 with the help of withColumn

# this is average()
df3.withColumn("Avg",
			avg(col("salary")).over(windowPartitionAgg))\
    .withColumn("Sum",sum(col("salary")).over(windowPartitionAgg))\
    .withColumn("Min",min(col("salary")).over(windowPartitionAgg))\
    .withColumn("Max",max(col("salary")).over(windowPartitionAgg)).show()






"""

df3.withColumn("Avg", 
               avg(col("salary")).over(windowPartitionAgg))
    #this is sum()
  .withColumn("Sum",
              sum(col("salary")).over(windowPartitionAgg))
    #this is min()
  .withColumn("Min",
              min(col("salary")).over(windowPartitionAgg))
    #this is max()
  .withColumn("Max", 
              max(col("salary")).over(windowPartitionAgg)).show()

"""
