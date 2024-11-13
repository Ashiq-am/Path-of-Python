# importing the library and
# its SparkSession functionality
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row

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

# Getting RDD object from the DataFrame
rdd = df.rdd

# Taking a single sample of from the RDD
# Putting num = 1 in the takeSample() function
rdd_sample = rdd.takeSample(withReplacement=False,
							num=1)
print(rdd_sample)
