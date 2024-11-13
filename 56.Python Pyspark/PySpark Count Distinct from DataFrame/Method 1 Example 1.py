# importing module
import pyspark

# importing sparksession from
# pyspark.sql mudule
from pyspark.sql import SparkSession

# creating sparksession and giving
# app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# giving rows value for dataframe
data = [("Ram", "MCA", 80),
		("Riya", "MBA", 85),
		("Jiya", "B.E", 60),
		("Maria", "B.Tech", 65),
		("Shreya", "B.sc", 91),
		("Ram", "MCA", 80),
		("John", "M.E", 85),
		("Shyam", "BA", 70),
		("Kumar", "B.sc", 78),
		("Maria", "B.Tech", 65)]

# giving column names of dataframe
columns = ["Name", "Course", "Marks"]

# creating a dataframe df
df = spark.createDataFrame(data, columns)

# show df
df.show()

# counting the total number of values
# in df
print("Total number of records in df:", df.count())
