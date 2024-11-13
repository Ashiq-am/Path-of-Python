# findspark
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql import SparkSession
import findspark


findspark.init('c:/spark')

# initialize the data
data = [
	(("Pulkit", "Dhingra"), 12, "CS32", 82, "Programming"),
	(("Ritika", "Pandey"), 20, "CS32", 94, "Writing"),
	(("Atirikt", "Sans"), 4, "BB21", 78, None),
	(("Reshav", None), 18, None, 56, None)
]

# start spark session
spark = SparkSession.builder.appName("Student_Info").getOrCreate()

# initialize the schema of the data
schema = StructType([
	StructField('name', StructType([
		StructField('firstname', StringType(), True),
		StructField('lastname', StringType(), True)
	])),
	StructField("Roll Number", IntegerType(), True),
	StructField("Class ID", StringType(), True),
	StructField("Marks", IntegerType(), True),
	StructField("Extracurricular", StringType(), True)
])
# create a dataframe
df2 = spark.createDataFrame(data=data, schema=schema)

# display the schema
df2.printSchema()

# select operation
df2.select("name.firstname", "name.lastname").show(truncate=False)

# stop session
spark.stop()
