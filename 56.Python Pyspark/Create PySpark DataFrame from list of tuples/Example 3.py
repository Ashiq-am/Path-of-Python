# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

#list of tuples of plants data
data = [("mango", "AP", "Guntur"),
		("mango", "AP", "Chittor"),
		("sugar cane", "AP", "amaravathi"),
		("paddy", "TS", "adilabad"),
		("wheat", "AP", "nellore")]

# giving column names of dataframe
columns = ["Crop Name", "State", "District"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

#count records in the list
dataframe.count()
