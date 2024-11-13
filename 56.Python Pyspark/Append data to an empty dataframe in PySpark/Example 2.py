# Importing PySpark and the SparkSession,
# DataType functionality
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Creating a spark session
spark_session = SparkSession.builder.appName(
	'Spark_Session').getOrCreate()

# Creating an empty RDD to make a DataFrame
# with no data
emp_RDD = spark_session.sparkContext.emptyRDD()

# Defining the schema of the DataFrame
columns = StructType([StructField('Stadium', StringType(), False),
					StructField('Capacity', IntegerType(), False)])

# Creating an empty DataFrame
df = spark_session.createDataFrame(data=emp_RDD,
								schema=columns)

# Printing the DataFrame with no data
df.show()

# Hardcoded row for the second DataFrane
added_row = [['Motera Stadium', 132000]]

# Creating the DataFrame
added_df = spark_session.createDataFrame(added_row, columns)

# Storing the union of first_df and second_df
# in first_df
df = df.union(added_df)

# Our first DataFrame that was empty,
# now has data
df.show()
