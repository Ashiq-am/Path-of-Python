# importing necessary libraries
from pyspark.sql import SparkSession
import pyspark.sql.types as T

# function to create SparkSession
def create_session():
	spk = SparkSession.builder \
		.master("local") \
		.appName("Product_mart.com") \
		.getOrCreate()
	return spk

# function to create dataframe
def create_df(spark, data, schema):
	df1 = spark.createDataFrame(data, schema)
	return df1


if __name__ == "__main__":

	# calling function to create SparkSession
	spark = create_session()

	# Data containing the Array and Map- key,value pair
	input_data = [
		("Alex", 'Buttler', ["Mathematics", "Computer Science"],
		{"Mathematics": 'Physics', "Chemistry": "Biology"}),
		("Sam", "Samson", ["Chemistry, Biology"],
		{"Chemistry": 'Physics', "Mathematics": "Biology"}),
		("Rossi", "Bryant", ["English", "Geography"],
		{"History": 'Geography', "Chemistry": "Biology"}),
		("Sidz", "Murraz", ["History", "Environmental Science"],
		{"English": 'Environmental Science', "Chemistry": "Mathematics"}),
		("Robert", "Cox", ["Physics", "English"],
		{"Computer Science": 'Environmental Science', "Chemistry": "Geography"})
	]

	# defining schema with ArrayType and MapType()
	# using StructType() and StructField()
	array_schm = StructType([
		StructField('Firstname', StringType(), True),
		StructField('Lastname', StringType(), True),
		StructField('Subject', ArrayType(StringType()), True),
		StructField('Subject Combinations', MapType(
			StringType(), StringType()), True)
	])

	# calling function for creating the dataframe
	df = create_df(spark, input_data, array_schm)

	# printing schema of df and showing dataframe
	df.printSchema()
	df.show(truncate=False)
