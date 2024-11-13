# Pyspark convert multiple columns to map

# Import the libraries SparkSession, col, lit, create_map
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,lit,create_map

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
data_frame=csv_file = spark_session.read.csv(
'/content/class_data.csv',
sep = ',', inferSchema = True, header = True)

# Convert name, class and fees columns to map
data_frame = data_frame.withColumn(
"student_details",create_map(lit("student_name"),
col("name"), lit("student_class"),col("class"),
lit("student_fees"),col("fees"))).drop("name",
										"class",
										"fees")

# Display the data frame
data_frame.show(truncate=False)
