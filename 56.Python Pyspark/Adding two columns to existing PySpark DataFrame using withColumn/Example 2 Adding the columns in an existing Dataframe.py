# import pandas to read json file
import pandas as pd

# importing module
import pyspark

# importing sparksession from pyspark.sql
# module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()


# create Dataframe
df = spark.read.option("header",True).csv("Cricket_data_set_odi.csv")

# Display Schema
df.printSchema()

# Show Dataframe
df.show()
