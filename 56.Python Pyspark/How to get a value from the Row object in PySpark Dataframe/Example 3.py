# library imports are done here
import pyspark
from pyspark.sql import SparkSession

# Session Creation
random_value_session = SparkSession.builder.appName(
	'Random_Value_Session'
).getOrCreate()

# Data filled in our DataFrame
# Rows below will be filled
rows = [['Denmark Open', 'October', 'Super 1000'],
		['Indonesia Open', 'June', 'Super 1000'],
		['Korea Open', 'April', 'Super 500'],
		['Japan Open', 'August', 'Super 750'],
		['Akita Masters', 'July', 'Super 100']]

# DataFrame Columns
columns = ['Tournament', 'Month', 'Level']

# DataFrame creation
dataframe = random_value_session.createDataFrame(rows,
												columns)

# DataFrame print
dataframe.show()

# list of rows using collect()
row_list = dataframe.collect()

# Lets take the third Row object
row_object = row_list[2]

# If we imagine it as a Python List,
# We can get the first value of the list,
# index 0, let's try it
print(row_object[0])

# We got the value of column at index 0
# which is - 'Tournament'

# A few more examples
print(row_list[4][0])
print(row_list[3][1])
print(row_list[4][2])
