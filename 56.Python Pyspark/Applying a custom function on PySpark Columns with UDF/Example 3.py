# Python program to apply a custom
# function on PySpark Columns with UDF

# Import the libraries SparkSession, functions, types
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pyspark.sql.types as T

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a data frame with duplicate column names
df = spark_session.createDataFrame(
[('Arun',1,2,3),('Aniket',4,5,6),
				('Ishita',7,8,9)],
['name','maths_marks','science_marks',
						'english_marks'])

# Applying a custom function on PySpark Columns with UDF
percentage=F.udf(lambda a,b,c: ((a+b+c)/30)*100,
								T.FloatType())

# Display the data frame with new column calling the
# percentage function with marks as arguments
updated_df = df.withColumn('Percentage',
			percentage('maths_marks', 'science_marks',
									'english_marks') )

# Display the updated data frame
updated_df.show()
