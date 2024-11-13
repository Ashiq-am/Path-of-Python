# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of tuples of college data
data = [("sravan", "IT", 80),
		("jyothika", "CSE", 85),
		("harsha", "ECE", 60),
		("thanmai", "IT", 65),
		("durga", "IT", 91)]

# giving column names of dataframe
columns = ["Name", "Branch", "Percentage"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

# show data frame
dataframe.show()
