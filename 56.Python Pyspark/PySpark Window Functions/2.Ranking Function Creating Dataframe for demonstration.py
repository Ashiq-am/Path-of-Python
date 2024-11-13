# importing pyspark
from pyspark.sql.window import Window
import pyspark

# importing sparksessio
from pyspark.sql import SparkSession

# creating a sparksession object and providing appName
spark = SparkSession.builder.appName("pyspark_window").getOrCreate()

# sample data for dataframe
sampleData = ((101, "Ram", "Biology", 80),
			(103, "Meena", "Social Science", 78),
			(104, "Robin", "Sanskrit", 58),
			(102, "Kunal", "Phisycs", 89),
			(101, "Ram", "Biology", 80),
			(106, "Srishti", "Maths", 70),
			(108, "Jeny", "Physics", 75),
			(107, "Hitesh", "Maths", 88),
			(109, "Kailash", "Maths", 90),
			(105, "Sharad", "Social Science", 84)
			)

# column names for dataframe
columns = ["Roll_No", "Student_Name", "Subject", "Marks"]

# creating the dataframe df
df2 = spark.createDataFrame(data=sampleData,
							schema=columns)

# importing window from pyspark.sql.window

# creating a window partition of dataframe
windowPartition = Window.partitionBy("Subject").orderBy("Marks")

# print schema
df2.printSchema()

# show df
df2.show()
