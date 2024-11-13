# Python program to illustrate the working
# of unionByName() function with an
# additional argument

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('GeeksforGeeks.com').getOrCreate()

# Creating a dataframe
data_frame1 = spark.createDataFrame(
	[("Bhuwanesh", 82.98, "Computer Science"),
	("Harshit", 80.31, "Information Technology")],
	["Student Name", "Overall Percentage", "Department"]
)

# Creating another dataframe
data_frame2 = spark.createDataFrame(
	[("Naveen", 91.123), ("Piyush", 90.51)],
	["Student Name", "Overall Percentage"]
)

# Union both the dataframes using unionByName() method
res = data_frame1.unionByName(data_frame2, allowMissingColumns=True)

# Print the result of the union()
res.show()
