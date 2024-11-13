# importing module
import pyspark

# import concat_ws and lit function
from pyspark.sql.functions import concat_ws, lit

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of employee data
data = [["1", "sravan", "company 1"],
		["2", "ojaswi", "company 1"],
		["3", "rohith", "company 2"],
		["4", "sridevi", "company 1"],
		["5", "bobby", "company 1"]]

# specify column names
columns = ['ID', 'NAME', 'Company']

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# add salary column by checking its existance
if 'salary' not in dataframe.columns:
	dataframe.withColumn("salary", lit(34000)).show()
