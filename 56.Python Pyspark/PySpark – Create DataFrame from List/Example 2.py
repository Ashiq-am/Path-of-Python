# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data with two lists
data = [["node.js", "dbms", "integration"],
		["jsp", "SQL", "trigonometry"],
		["php", "oracle", "statistics"],
		[".net", "db2", "Machine Learning"]]

# giving column names of dataframe
columns = ["Web Technologies", "Data bases", "Maths"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

# show data frame
dataframe.show()
