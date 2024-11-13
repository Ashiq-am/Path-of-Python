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

# Converting the DataFrame to
# a Pandas DataFrame and taking a sample row
pandas_random = df.toPandas().sample()

# Converting the sample into
# a PySpark DataFrame
df_random = random_row_session.createDataFrame(pandas_random)

# Showing our randomly selected row
df_random.show()
