# Python program to apply a transformation to multiple
# columns of PySpark dataframe using reduce function

# Import the SparkSession, reduce, col and upper libraries
from pyspark.sql import SparkSession
from functools import reduce
from pyspark.sql.functions import col, upper

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
data_frame=csv_file = spark_session.read.csv(
		'/content/student_data.csv',
		sep = ',', inferSchema = True,
		header = True)

# Apply a transformation to multiple columns of
# PySpark dataframe using reduce function
updated_data_frame = (reduce(lambda traverse_df,
col_name: traverse_df.withColumn(col_name,
upper(col(col_name))), data_frame.columns,
						data_frame))

# Show the updated data frame
updated_data_frame.show()
