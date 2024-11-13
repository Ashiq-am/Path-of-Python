# Python program to apply a transformation to multiple
# columns of PySpark dataframe using for loop

# Import the SparkSession, col and upper libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
data_frame=csv_file = spark_session.read.csv(
		'/content/student_data.csv',
		sep = ',', inferSchema = True,
		header = True)

# Apply a transformation to multiple
# columns of PySpark dataframe using for loop
for col_name in data_frame.columns:
	data_frame = data_frame.withColumn(col_name,
						upper(col(col_name)))

# Show the updated data frame
data_frame.show()
