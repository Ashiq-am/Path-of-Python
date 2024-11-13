# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of dictionaries of students data
data = [{"Student ID": 1, "Student name": "sravan"},
		{"Student ID": 2, "Student name": "Jyothika"},
		{"Student ID": 3, "Student name": "deepika"},
		{"Student ID": 4, "Student name": "harsha"}]

# creating a dataframe
dataframe = spark.createDataFrame(data)

# display dataframe
dataframe.show()
