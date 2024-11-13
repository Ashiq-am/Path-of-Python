# installing pyspark
#!pip install pyspark

# importing pyspark
import pyspark

# importing SparkSession
from pyspark.sql import SparkSession

# importing all from pyspark.sql.function
from pyspark.sql.functions import *

# creating SparkSession object
spark=SparkSession.builder.appName("sparkdf").getOrCreate()


# creating the row data for dataframe
data = [('Jaya', 'Sinha', 'F', '1991-04-01'),
		('Milan', 'Sharma', '', '2000-05-19'),
		('Rohit', 'Verma', 'M', '1978-09-05'),
		('Maria', 'Anne', 'F', '1967-12-01'),
		('Jay', 'Mehta', 'M', '1980-02-17')
		]

# giving the column names for the dataframe
columns = ['First Name', 'Last Name', 'Gender', 'DOB']

# creating the dataframe df
df = spark.createDataFrame(data, columns)

# printing dataframe schema
df.printSchema()

# show dataframe
df.show()
