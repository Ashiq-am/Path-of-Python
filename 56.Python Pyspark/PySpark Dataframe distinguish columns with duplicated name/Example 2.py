# PySpark program to distinguish columns with duplicated name

# Import the library SparkSession
from pyspark.sql import SparkSession

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a data frame with duplicate column names
df = spark_session.createDataFrame(
[('Arun',1,2,3),('Aniket',4,5,6),
('Ishita',7,8,9)],
['name','marks','marks','marks'])

# Store all the column names in the list
df_cols = df.columns

# Get index of the duplicate columns
duplicate_col_index = [idx for idx,
val in enumerate(df_cols) if val in df_cols[:idx]]

# Create a new list by renaming duplicate
# columns by adding prefix '_duplicate_'+index
for i in duplicate_col_index:
	df_cols[i] = df_cols[i] + '_duplicate_'+ str(i)

# Rename the duplicate columns in data frame
df = df.toDF(*df_cols)

# Define a function to do sum
sum_marks=lambda a,b,c: a+b+c

# Display the data frame with new column calling
# the sum_marks function with marks as arguments
df.withColumn('Sum of Marks',
			sum_marks(df.marks,df.marks_duplicate_2,
						df.marks_duplicate_3) ).show()
