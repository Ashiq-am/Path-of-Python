# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [[1, "sravan", "company 1"], [2, "ojaswi", "company 1"],
		[3, "rohith", "company 2"], [4, "sridevi", "company 1"],
		[1, "sravan", "company 1"], [4, "sridevi", "company 1"]]

# specify column names
columns = ['ID', 'NAME', 'Company']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# select all columns e where name = sridevi
dataframe.select(['ID', 'NAME', 'Company']).where(
	dataframe.NAME == 'sridevi').show()
