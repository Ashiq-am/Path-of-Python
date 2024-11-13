# importing module
import pyspark

# importing sparksession from pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()


# Column names for the dataframe
columns = ["LicenseNo", "ExpiryDate"]

# Row data for the dataframe
data = [
	("MH201411094334", "2024-11-19"),
	("AR202027563890", "2030-03-16"),
	("UP202010345567", "2035-12-30"),
	("KN201822347800", "2028-10-29"),
]

# Create the dataframe using the above values
reg_df = spark.createDataFrame(data=data,
							schema=columns)

# View the dataframe
reg_df.show()
