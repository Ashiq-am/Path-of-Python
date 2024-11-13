# importing module
from pyspark.sql import SparkSession, Row

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# create 2 Rows with 3 columns
data = Row(First_name="Sravan", Last_name="Kumar", age=23),
Row(First_name="Ojaswi", Last_name="Pinkey", age=16),
Row(First_name="Rohith", Last_name="Devi", age=7)

# create row on rdd
rdd = spark.sparkContext.parallelize(data)

# display data
rdd.collect()
