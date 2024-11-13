# Python program to apply a custom
# function on PySpark Columns with UDF

# Import the libraries SparkSession, functions, types and date
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T
from datetime import date

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Read the CSV file
df=csv_file = spark_session.read.csv('/content/student_data.csv',
			sep = ',', inferSchema = True,
						header = True)

# Get current year
current_year=date.today().year

# Applying a custom function on PySpark Columns with UDF
birth_year = F.udf(lambda age: current_year-age,
				T.StringType())

# Create new column for calculating the birth year
updated_df = df.withColumn('Birth Year',
						birth_year('age'))

# Display the updated data frame
updated_df.show()
