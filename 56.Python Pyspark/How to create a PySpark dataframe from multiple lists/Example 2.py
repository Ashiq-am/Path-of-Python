# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data with dictionary
# with four lists in three elements each
data = [1, 2, 3]
data1 = ["sravan", "bobby", "ojaswi"]
data2 = ["iit-k", "iit-mumbai", "vignan university"]
data3 = ["AP", "TS", "UP"]

# specify column names
columns = ['ID', 'NAME', 'COLLEGE', 'ADDRESS']

# creating a dataframe by zipping
# the two lists
dataframe = spark.createDataFrame(
zip(data, data1, data2, data3), columns)

# show data frame
dataframe.show()
