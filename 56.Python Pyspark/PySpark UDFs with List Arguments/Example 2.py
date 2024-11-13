# Import the libraries SparkSession, SQLContext, UDF, col, StringType
from pyspark.sql import SQLContext, SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

# Create a spark session using getOrCreate() function
spark_session = SparkSession.builder.getOrCreate()

# Create a spark context
sc=spark_session.sparkContext

# Create a SQL context
sqlContext= SQLContext(sc)

# Create the data frame using createDataFrame function
data_frame= sqlContext.createDataFrame([("Ashish", 92),
										("Mehak", 74),
										("Ishita", 83),
										("Arun",54)],
									["Name", "Marks"])

# Create a list to be passed as parameter
Remarks_List = ["Excellent", "Good", "Can do better"]

# Create a function to pass list as default value to a variable
def parameter_udf( marks_index,label=Remarks_List):
	if marks_index >85:
		return label[0]
	elif marks_index > 75:
		return label[1]
	elif marks_index >60:
		return label[2]
	else:
		return 'Needs Improvement'

# Create a user defined function with parameters
# parameter_udf and column type.
udfcate = udf(parameter_udf, StringType())

# Create a column by calling the user defined function
# created above and display data frame
data_frame.withColumn("Remarks", udfcate("Marks")).show()
