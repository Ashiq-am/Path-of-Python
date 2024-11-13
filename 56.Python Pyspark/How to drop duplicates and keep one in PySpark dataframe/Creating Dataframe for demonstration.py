# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Start spark session
spark = SparkSession.builder.appName("Student_Info").getOrCreate()

# Initialize our data
data2 = [("Pulkit", 12, "CS32", 82, "Programming"),
		("Ritika", 20, "CS32", 94, "Writing"),
		("Ritika", 20, "CS32", 84, "Writing"),
		("Atirikt", 4, "BB21", 58, "Doctor"),
		("Atirikt", 4, "BB21", 78, "Doctor"),
		("Ghanshyam", 4, "DD11", 38, "Lawyer"),
		("Reshav", 18, "EE43", 56, "Timepass")
		]

# Define schema
schema = StructType([
	StructField("Name", StringType(), True),
	StructField("Roll Number", IntegerType(), True),
	StructField("Class ID", StringType(), True),
	StructField("Marks", IntegerType(), True),
	StructField("Extracurricular", StringType(), True)
])

# read the dataframe
df = spark.createDataFrame(data=data2, schema=schema)
df.show()
