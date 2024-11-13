from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql import SparkSession
import findspark


# spark location
# add the respective path to your spark
findspark.init('_path-to-spark_')

# Initialize our data
data2 = [("Pulkit", 12, "CS32", 82, "Programming"),
		("Ritika", 20, "CS32", 94, "Writing"),
		("Atirikt", 4, "BB21", 78, None),
		("Reshav", 18, None, 56, None)
		]

# Start spark session
spark = SparkSession.builder.appName("Student_Info").getOrCreate()

# Define schema
schema = StructType([
	StructField("Name", StringType(), True),
	StructField("Roll Number", IntegerType(), True),
	StructField("Class ID", StringType(), True),
	StructField("Marks", IntegerType(), True),
	StructField("Extracurricular", StringType(), True)
])

# create the dataframe
df = spark.createDataFrame(data=data2, schema=schema)

# drop None Values
df.na.drop(subset=["Class ID"]).show(truncate=False)

# stop spark session
spark.stop()
