# Pyspark program to updated nested columns

# Import the libraries SparkSession, StructType,
# StructField, StringType, IntegerType, col, lit, when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import col, lit, when
from pyspark.sql import SparkSession

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Define the data set
data_set = [((2000,21,2),18),
			((1998,14,6),24),
			((1998,1,11),18),
			((2006,30,3),16)]

# Define the structure for the data frame
schema = StructType([StructField('Date_Of_Birth',
			StructType([StructField('Year', IntegerType(), True),
			StructField('Month', IntegerType(), True),
			StructField('Date', IntegerType(), True) ])),
			StructField('Age', IntegerType(), True)])

# Create the Pyspark data frame using createDataFramr function
df = spark_session.createDataFrame(data = data_set,
								schema = schema)

# Update nested column using lit function with specific
# condition using when and otherwise function
updated_df = df.withColumn("Date_Of_Birth",
				col("Date_Of_Birth").withField("Year",
				when (col("Age")==18,
				lit(2004)).otherwise(
				lit(col("Date_Of_Birth.Year")))))

# Display the updated data frame
updated_df.show()
