# importing the library and
# its SparkSession functionality
import pyspark
from pyspark.sql import SparkSession

# creating a session to make DataFrames
random_row_session = SparkSession.builder.appName(
	'Random_Row_Session'
).getOrCreate()

# Pre-set data for our DataFrame
data = [['a', 1], ['b', 2], ['c', 3], ['d', 4]]
columns = ['Letters', 'Position']

# Creating a DataFrame
df = random_row_session.createDataFrame(data,
										columns)

# Printing the DataFrame
df.show()

# Taking a sample of df and storing it in #df2
# please not that the second argument here is a fraction
# of the data set we need(fraction is in float)
# number of rows = fraction * total number of rows
df2 = df.sample(False, 1.0/len(df.collect()))

# printing the sample row which is a DataFrame
df2.show()
