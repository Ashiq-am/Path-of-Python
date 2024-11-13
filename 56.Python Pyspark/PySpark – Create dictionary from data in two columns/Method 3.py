# importing pyspark
# make sure you have installed the pyspark library
import pyspark

# Importing and creating a SparkSession to work on
# DataFrames The session name is 'Practice_Session'
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

result = {}

# Convert PySpark DataFrame to Pandas
# DataFrame
df_pandas = df_pyspark.toPandas()

# Traverse through each column
for column in df_pandas.columns:

	# Add key as column_name and
	# value as list of column values
	result[column] = df_pandas[column].values.tolist()

# Print the dictionary
print(result)
