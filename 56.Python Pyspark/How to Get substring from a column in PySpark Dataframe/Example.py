# importing necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, substring


# function to create new SparkSession
def create_session():
	spk = SparkSession.builder \
		.master("local") \
		.appName("Substring.com") \
		.getOrCreate()
	return spk

def create_df(spark, data, schema):

	df1 = spark.createDataFrame(data, schema)
	return df1

if __name__ == "__main__":

	input_data = [("India", +91, 2701, 2020),
				("United States of America", +1, 1301, 2020),
				("Israel", +972, 3102, 2020),
				("Dubai", +971, 2901, 2020),
				("Russia", 7, 3101, 2020)]

	# calling function to create SparkSession
	spark = create_session()

	schema = ["Country", "Country Code",
			"Data", "Year"]

	# calling function to create dataframe
	df = create_df(spark, input_data, schema)
	df.show()
