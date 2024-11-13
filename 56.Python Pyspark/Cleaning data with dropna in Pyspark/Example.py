# importing necessary libraries
from pyspark.sql import SparkSession

# function to create new SparkSession
def create_session():
	spk = SparkSession.builder \
		.master("local") \
		.appName("Employee_detail.com") \
		.getOrCreate()
	return spk


def create_df(spark, data, schema):
	df1 = spark.createDataFrame(data, schema)
	return df1


if __name__ == "__main__":

	# calling function to create SparkSession
	spark = create_session()

	input_data = [(1, "Shivansh", "Data Scientist", "Noida"),
				(2, None, "Software Developer", None),
				(3, "Swati", "Data Analyst", "Hyderabad"),
				(4, None, None, "Noida"),
				(5, "Arpit", "Android Developer", "Banglore"),
				(6, "Ritik", None, None),
				(None, None, None, None)]
	schema = ["Id", "Name", "Job Profile", "City"]

	# calling function to create dataframe
	df = create_df(spark, input_data, schema)
	df.show()
