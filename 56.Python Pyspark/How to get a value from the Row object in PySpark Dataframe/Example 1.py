# library import
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

# Session Creation
random_value_session = SparkSession.builder.appName(
	'Random_Value_Session'
).getOrCreate()

# Data filled in our DataFrame
# 5 rows below
rows = [['All England Open', 'March', 'Super 1000'],
		['Malaysia Open', 'January', 'Super 750'],
		['Korea Open', 'April', 'Super 500'],
		['Hylo Open', 'November', 'Super 100'],
		['Spain Masters', 'March', 'Super 300']]

# Columns of our DataFrame
columns = ['Tournament', 'Month', 'Level']

#DataFrame is created
dataframe = random_value_session.createDataFrame(rows,
												columns)

# Showing the DataFrame
dataframe.show()

# getting list of rows using collect()
row_list = dataframe.collect()

# Printing the first Row object
# from which data is extracted
print(row_list[0])

# Using __getitem__() magic method
# To get value corresponding to a particular
# column
print(row_list[0].__getitem__('Level'))
print(row_list[0].__getitem__('Tournament'))
print(row_list[0].__getitem__('Level'))
print(row_list[0].__getitem__('Month'))
