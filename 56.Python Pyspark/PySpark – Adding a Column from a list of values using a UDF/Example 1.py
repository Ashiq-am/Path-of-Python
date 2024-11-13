# PySpark - Adding a Column from a
# list of values using a UDF

# Import the libraries SparkSession,
# functions, IntegerType,
# StringType, row_number,
# monotonically_increasing_id and Window
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import IntegerType, StringType
from pyspark.sql.functions import row_number, monotonically_increasing_id
from pyspark.sql.window import Window

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a user defined function to assign student names
# according to the row index by subtracting row number from 1
labels_udf = F.udf(lambda indx: student_names[indx-1], StringType())

# Create a data frame with three columns 'Roll_Number,' 'Fees' and 'Fine'
df = spark_session.createDataFrame(
	[(1, 10000, 400), (2, 14000, 500), (3, 12000, 800)],
['Roll_Number', 'Fees', 'Fine'])

# Define a list of elements
student_names = ['Aman', 'Ishita', 'Vinayak']

# Create a column with continuous increasing Id's
df = df.withColumn("num_id", row_number().over(
	Window.orderBy(monotonically_increasing_id())))

# Create a new column by calling the user defined function
new_df = df.withColumn('Names', labels_udf('num_id'))

# Delete the increasing Id's column and display the data frame
new_df.drop('num_id').show()
