# importing module
import pyspark

# import when and lit function
from pyspark.sql.functions import when, lit

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [["1", 23],
		["2", 21],
		["3", 32],
		]

# specify column names
columns = ['ID', 'Age']

# creating a dataframe from the lists of data
dataframe2 = spark.createDataFrame(data, columns)

# display
dataframe2.show()
