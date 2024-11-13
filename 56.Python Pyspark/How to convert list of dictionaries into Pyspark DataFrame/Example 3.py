# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of dictionaries of crop data
data = [{"Crop ID": 1, "name": "rose", "State": "AP"},
		{"Crop ID": 2, "name": "lilly", "State": "TS"},
		{"Crop ID": 3, "name": "lotus", "State": "Maharashtra"},
		{"Crop ID": 4, "name": "jasmine", "State": "AP"}]

# creating a dataframe
dataframe = spark.createDataFrame(data)

# display dataframe count
dataframe.count()
