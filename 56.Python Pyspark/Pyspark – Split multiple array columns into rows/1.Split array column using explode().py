# importing pyspark
import pyspark

# importing sparksessio
from pyspark.sql import SparkSession

# importing all from pyspark.sql.functions
# like Row, array, explode etc.
from pyspark.sql.functions import *

# creating a sparksession object and
# providing appName
spark=SparkSession.builder.appName("sparkdf").getOrCreate()

# now creating dataframe
# creating the row data and giving array
# values for dataframe
data = [('Jaya', '20', ['SQL','Data Science']),
		('Milan', '21', ['ML','AI']),
		('Rohit', '19', ['Programming', 'DSA']),
		('Maria', '20', ['DBMS', 'Networking']),
		('Jay', '22', ['Data Analytics','ML'])]

# column names for dataframe
columns = ['Name', 'Age', 'Courses_enrolled']

# creating dataframe with createDataFrame()
df = spark.createDataFrame(data, columns)

# printing dataframe schema
df.printSchema()

# show dataframe
df.show()
