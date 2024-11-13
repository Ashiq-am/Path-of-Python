# importing pyspark
# make sure you have installed the pyspark library
import pyspark

# Importing and creating a SparkSession
# to work on DataFrames
# The session name is 'Practice_Session'
from pyspark.sql import SparkSession
spark_session = SparkSession.builder.appName(
'Practice_Session').getOrCreate()

# Creating a DataFrame using createDataFrame()
# method, with hard coded data.
rows = [['John', 54],
		['Adam', 65],
		['Michael', 56],
		['Kelsey', 37],
		['Chris', 49],
		['Jonathan', 28],
		['Anthony', 26],
		['Esther', 48],
		['Rachel', 52],
		['Joseph', 56],
		['Richard', 49],
		]

columns = ['Name', 'Age']
df_pyspark = spark_session.createDataFrame(rows, columns)

# printing the DataFrame
df_pyspark.show()

# dictionary comprehension is used here
# Name column here is the key while Age
# columns is the value
# You can also use {row['Age']:row['Name']
# for row in df_pyspark.collect()},
# to reverse the key,value pairs


# collect() gives a list of
# rows in the DataFrame
result_dict = {row['Name']: row['Age']
			for row in df_pyspark.collect()}

# Printing a few key:value pairs of
# our final resultant dictionary
print(result_dict['John'])
print(result_dict['Michael'])
print(result_dict['Adam'])
