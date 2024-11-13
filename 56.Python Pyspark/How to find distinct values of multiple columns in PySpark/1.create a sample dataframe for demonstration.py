# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [["1", "Tezas", "Google"],
		["2", "Mohit Rawat", "Rakuten"],
		["3", "rohith", "Geeksforgeeks"],
		["4", "Nancy", "IBM"],
		["1", "Raghav", "Wipro"],
		["4", "Komal", "Amazon"]]

# specify column names
columns = ['ID', 'NAME', 'Company']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

dataframe.show()
