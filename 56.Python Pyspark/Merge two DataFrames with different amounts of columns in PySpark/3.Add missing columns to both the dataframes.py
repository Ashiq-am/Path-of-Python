# importing module
import pyspark

# import lit function
from pyspark.sql.functions import lit

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

# list of employee data
data = [["1", 23],
		["2", 21],
		["3", 32],
		]

# specify column names
columns = ['ID', 'Age']

# creating a dataframe from the lists of data
dataframe2 = spark.createDataFrame(data, columns)

# add columns in dataframe1 that are missing from dataframe2
for column in [column for column in dataframe2.columns
			if column not in dataframe1.columns]:
	dataframe1 = dataframe1.withColumn(column, lit(None))

# add columns in dataframe2 that are missing from dataframe1
for column in [column for column in dataframe1.columns
			if column not in dataframe2.columns]:
	dataframe2 = dataframe2.withColumn(column, lit(None))

# now see the columns of dataframe1
print(dataframe1.columns)

# now see the columns of dataframe2
print(dataframe2.columns)
