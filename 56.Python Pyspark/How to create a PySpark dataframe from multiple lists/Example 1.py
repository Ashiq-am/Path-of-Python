# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data with dictionary
# with two lists in three elements each
data = [1, 2, 3]
data1 = ["sravan", "bobby", "ojaswi"]

# specify column names
columns = ['ID', 'NAME']

# creating a dataframe by zipping the two lists
dataframe = spark.createDataFrame(zip(data, data1), columns)

# show data frame
dataframe.show()
