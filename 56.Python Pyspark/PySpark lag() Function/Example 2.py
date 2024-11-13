# PySpark - How to set the default value
# for pyspark.sql.functions.lag to
# a value within the current row?

# Import the SparkSession, Window and lag libraries
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import lag

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
data_frame = csv_file = spark_session.read.csv(
	'/content/student_data.csv', sep=',', inferSchema=True, header=True)

# Declare a list according to which partition has to be done
column_list = ["age", "class", "fees"]

# Partition data through list elements and sort it
# through age column in Window function
Windowspec = Window.partitionBy(column_list).orderBy("age")

# Calculating lag of subject by 1 for each student
# and putting in new column 'Updated Subject'
data_frame.withColumn('Updated Subject', lag(
	data_frame['subject'], 1, 'Same Subject').over(Windowspec)).show()
