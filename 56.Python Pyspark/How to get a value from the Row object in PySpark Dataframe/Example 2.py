# library imports are done here
import pyspark
from pyspark.sql import SparkSession

# Session Creation
random_value_session = SparkSession.builder.appName(
	'Random_Value_Session'
).getOrCreate()

# Data filled in our DataFrame
# Rows below will be filled
rows = [['French Open', 'October', 'Super 750'],
		['Macau Open', 'November', 'Super 300'],
		['India Open', 'January', 'Super 500'],
		['Odisha Open', 'January', 'Super 100'],
		['China Open', 'November', 'Super 1000']]

# DataFrame Columns
columns = ['Tournament', 'Month', 'Level']

# DataFrame creation
dataframe = random_value_session.createDataFrame(rows,
												columns)

# DataFrame print
dataframe.show()

# list of rows using collect()
row_list = dataframe.collect()

# Printing the second Row object
# from which we will read data
print(row_list[1])
print()

# Printing dictionary to make
# things more clear
print(row_list[1].asDict())
print()

# Using asDict() method to convert row object
# into a dictionary where the column names are keys
# Using column names as keys to get respective values
print(row_list[1].asDict()['Tournament'])
print(row_list[1].asDict()['Month'])
print(row_list[1].asDict()['Level'])
