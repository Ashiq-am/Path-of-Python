# importing module
import pyspark
from pyspark.sql import SparkSession
from pyspark.context import SparkContext

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# create DataFrame
df=spark.read.option(
"header",True).csv("Cricket_data_set_odi.csv")

# Display schema
df.printSchema()
