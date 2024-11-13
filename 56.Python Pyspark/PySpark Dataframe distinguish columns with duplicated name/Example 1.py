# Import the library SparkSession
from pyspark.sql import SparkSession

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a data frame with duplicate column names
df = spark_session.createDataFrame(
[('Monday',25,27,29,30),('Tuesday',40,38,36,34),
('Wednesday',18,20,22,17),('Thursday',25,27,29,19)],
['day','temperature','temperature',
'temperature','temperature'])

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

# Display the data frame
df.show()
