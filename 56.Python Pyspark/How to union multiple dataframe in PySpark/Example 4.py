# Python program to illustrate the
# working of unionByName() function

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('GeeksforGeeks.com').getOrCreate()

# Creating a data frame
data_frame1 = spark.createDataFrame(
	[("Bhuwanesh", 82.98), ("Harshit", 80.31)],
	["Student Name", "Overall Percentage"]
)

# Creating another data frame
data_frame2 = spark.createDataFrame(
	[(91.123, "Naveen"), (90.51, "Piyush"), (87.67, "Hitesh")],
	["Overall Percentage", "Student Name"]
)

# Union both the dataframes using unionByName() method
answer = data_frame1.unionByName(data_frame2)

# Print the combination of both the dataframes
answer.show()