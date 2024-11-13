# importing necessary libraries
from pyspark.sql import SparkSession


# function to create new SparkSession
def create_session():
	spk = SparkSession.builder \
		.master("local") \
		.appName("Product_details.com") \
		.getOrCreate()
	return spk

def create_df(spark, data, schema):
	df1 = spark.createDataFrame(data, schema)
	return df1


if __name__ == "__main__":

	input_data = [("Uttar Pradesh", 122000, 89600, 12238),
				("Maharashtra", 454000, 380000, 67985),
				("Tamil Nadu", 115000, 102000, 13933),
				("Karnataka", 147000, 111000, 15306),
				("Kerala", 153000, 124000, 5259)]

	# calling function to create SparkSession
	spark = create_session()

	schema = ["State", "Cases", "Recovered", "Deaths"]

	# calling function to create dataframe
	df = create_df(spark, input_data, schema)

	# visualizing the datframe
	df.show()
