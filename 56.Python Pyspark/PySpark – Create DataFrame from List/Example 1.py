# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data with two lists
data = [["java", "dbms", "python"],
		["OOPS", "SQL", "Machine Learning"]]

# giving column names of dataframe
columns = ["Subject 1", "Subject 2", "Subject 3"]

# creating a dataframe
dataframe = spark.createDataFrame(data, columns)

# show data frame
dataframe.show()
