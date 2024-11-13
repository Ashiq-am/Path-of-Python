# Create a spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkExamples').getOrCreate()

# Create a spark dataframe
columns = ["Name", "Course_Name",
		"Duration_Months",
		"Course_Fees", "Start_Date",
		"Payment_Done"]
data = [
	("Amit Pathak", "Python", 3,
	10000, "02-07-2021", True),
	("Shikhar Mishra", "Soft skills",
	2, 8000, "07-10-2021", False),
	("Shivani Suvarna", "Accounting",
	6, 15000, "20-08-2021", True),
	("Pooja Jain", "Data Science", 12,
	60000, "02-12-2021", False),
]
course_df = spark.createDataFrame(data).toDF(*columns)

# View the dataframe
course_df.show()
