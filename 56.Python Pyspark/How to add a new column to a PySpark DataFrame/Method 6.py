# importing module
import pyspark

# import when and lit function
from pyspark.sql.functions import when, lit

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

# add a new column named salary
# add value 34000 when name is sravan
# add value 31000 when name is ojsawi or bobby
# otherwise add 78000
dataframe.withColumn("salary",
					when((dataframe.NAME == "sravan"), lit("34000")).
					when((dataframe.NAME == "ojsawi") | (
						dataframe.NAME == "bobby"), lit("31000"))
					.otherwise(lit("78000"))).show()
