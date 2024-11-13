# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of college data with dictionary
# with three dictionaries
data = [{'student_id': 12, 'name': 'sravan', 'address': 'kakumanu'},
		{'student_id': 14, 'name': 'jyothika', 'address': 'tenali'},
		{'student_id': 11, 'name': 'deepika', 'address': 'repalle'}]

# creating a dataframe
dataframe = spark.createDataFrame(data)

# show data frame
dataframe.show()
