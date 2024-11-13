# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [(1, "sravan"), (2, "ojsawi"), (3, "bobby")]

# specify column names
columns = ['ID1', 'NAME1']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

dataframe.show()
