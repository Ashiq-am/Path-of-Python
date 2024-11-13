# importing module
import pyspark

# import when and lit function
from pyspark.sql.functions import when, lit

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [["1", "sravan", "kakumanu"],
		["2", "ojaswi", "hyd"],
		["3", "rohith", "delhi"],
		["4", "sridevi", "kakumanu"],
		["5", "bobby", "guntur"]]

# specify column names
columns = ['ID', 'NAME', 'Address']

# creating a dataframe from the lists of data
dataframe1 = spark.createDataFrame(data, columns)

# display
dataframe1.show()
