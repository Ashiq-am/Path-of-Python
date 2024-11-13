# Import the libraries SparkSession, SQLContext, UDF, col, StringType
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a spark context
sc = spark_session.sparkContext

# Create a SQL context
sqlContext = SQLContext(sc)

# Create the data frame using createDataFrame function
data_frame = sqlContext.createDataFrame(
	[("Ashish", 18), ("Mehak", 19), ("Ishita", 17),
	("Pranjal", 18), ("Arun", 16)], ["Name", "Age"])

# Create a list to be passed as parameter
Birth_Year = ["2004", "2003", "2005"]

# Create a function to pass list as default value to a variable


def parameter_udf(age_index, label=Birth_Year):
	if age_index == 18:
		return label[0]
	elif age_index == 17:
		return label[2]
	elif age_index == 19:
		return label[1]
	else:
		return 'Invalid'


# Create a user defined function with parameters
# parameter_udf and column type.
udfcate = udf(parameter_udf, StringType())

# Create a column by calling the user defined function
# created above and display data frame
data_frame.withColumn("Birth Year", udfcate("Age")).show()
