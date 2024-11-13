# PySpark - Adding a Column from a list of values using a UDF

# Import the libraries SparkSession, functions, IntegerType,
# StringType, row_number, monotonically_increasing_id and Window
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import IntegerType, StringType
from pyspark.sql.functions import row_number, monotonically_increasing_id
from pyspark.sql.window import Window

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a user defined function to assign student names
# according to the row index by subtracting row number from 1
labels_udf = F.udf(lambda indx: fine_data[indx-1], IntegerType())

# Read the CSV file
df = csv_file = spark_session.read.csv(
	'/content/student_data.csv', sep=',', inferSchema=True, header=True)

# Define a list of elements
fine_data = [200, 300, 400, 0, 500]

# Create a column with continuous increasing Id's
df = df.withColumn("num_id", row_number().over(
	Window.orderBy(monotonically_increasing_id())))

# Create a new column by calling the user defined function
new_df = df.withColumn('fine', labels_udf('num_id'))

# Delete the increasing Id's column and display the data frame
new_df.drop('num_id').show()
