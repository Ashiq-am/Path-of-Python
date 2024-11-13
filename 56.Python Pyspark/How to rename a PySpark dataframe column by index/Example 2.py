# importing module
import pyspark

# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# an app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# list of students data
data = [[123, "Sagar", "Rajveer", 22, "BBA"],
		[124, "Rajeev", "Mukesh", 23, "BBA"],
		[125, "Harish", "Parveen", 25, "BBA"],
		[126, "Gagan", "Rohit", 24, "BBA"],
		[127, "Rakesh", "Mayank", 25, "BBA"],
		[128, "Gnanesh", "Dleep", 26, "BBA"]]

# specify column names
columns = ['ID', 'Name', 'Father Name',
		'Age', "Course", ]

# creating a dataframe from the lists of data
dataframe = spark.createDataFrame(data, columns)

# display original dataframe
print('Actual data in dataframe')
dataframe.show()

# Rename column
df = dataframe.withColumnRenamed(dataframe.columns[1],
								"Student Name").withColumnRenamed(
	dataframe.columns[3], "Student Age")

# display dataframe after rename column
print('After rename 1 and 3 index column')
df.show()
