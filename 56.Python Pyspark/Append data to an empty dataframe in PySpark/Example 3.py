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

# Creating the DataFrame whose data
# needs to be added
added_df = spark_session.createDataFrame(added_row,
										columns)

# converting our PySpark DataFrames to
# Pandas DataFrames
pandas_added = added_df.toPandas()
df = df.toPandas()

# using append() function to add the data
df = df.append(pandas_added, ignore_index=True)

# reconverting our DataFrame back
# to a PySpark DataFrame
df = spark_session.createDataFrame(df)

# Printing resultant DataFrame
df.show()
