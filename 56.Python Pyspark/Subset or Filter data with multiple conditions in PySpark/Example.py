# importing necessary libraries
from pyspark.sql import SparkSession

# function to create SparkSession
def create_session():
	spk = SparkSession.builder \
		.master("local") \
		.appName("Student_report.com") \
		.getOrCreate()
	return spk


def create_df(spark, data, schema):
	df1 = spark.createDataFrame(data, schema)
	return df1


if __name__ == "__main__":

	# calling function to create SparkSession
	spark = create_session()

	input_data = [(1, "Shivansh", "Male", 20, 80),
				(2, "Arpita", "Female", 18, 66),
				(3, "Raj", "Male", 21, 90),
				(4, "Swati", "Female", 19, 91),
				(5, "Arpit", "Male", 20, 50),
				(6, "Swaroop", "Male", 23, 65),
				(7, "Reshabh", "Male", 19, 70)]
	schema = ["Id", "Name", "Gender", "Age", "Percentage"]

	# calling function to create dataframe
	df = create_df(spark, input_data, schema)
	df.show()
