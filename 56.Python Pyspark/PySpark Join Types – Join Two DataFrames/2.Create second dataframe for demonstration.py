# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data1 = [["1", "45000", "IT"],
		["2", "145000", "Manager"],
		["6", "45000", "HR"],
		["5", "34000", "Sales"]]

# specify column names
columns = ['ID', 'salary', 'department']

# creating a dataframe from the lists of data
dataframe1 = spark.createDataFrame(data1, columns)

dataframe1.show()
