# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [(1, "sravan"), (2, "ojsawi"),
		(3, "bobby"),
		(4, "rohith"), (5, "gnanesh")]

# specify column names
columns = ['ID2', 'NAME2']

# creating a dataframe from the lists of data
dataframe1 = spark.createDataFrame(data, columns)

dataframe1.show()
