# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data
data = [["1", "bobby", "vvit"],
		["2", "sravan", "jntuk"],
		["3", "rohith", "AU"],
		["4", "sridevi", "GVRS"],
		["1", "bobby", "vvit"]]

# specify column names
columns = ['ID', 'NAME', 'COLLEGE']

# creating a dataframe from the
# lists of data
dataframe = spark.createDataFrame(data, columns)

print('Actual data in dataframe')
dataframe.show()
