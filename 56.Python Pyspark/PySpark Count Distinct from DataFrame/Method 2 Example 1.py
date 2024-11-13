# importing sparksession from
# pyspark.sql mudule
from pyspark.sql import SparkSession

# creating sparksession and giving
# app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# giving rows value for dataframe
data = [("Ram", "IT", 80000),
		("Shyam", "Sales", 70000),
		("Jiya", "Sales", 60000),
		("Maria", "Accounts", 65000),
		("Ramesh", "IT", 80000),
		("John", "Management", 80000),
		("Shyam", "Sales", 70000),
		("Kumar", "Sales", 78000),
		("Maria", "Accounts", 65000)]

# giving column names of dataframe
columns = ["Emp_name", "Depart", "Salary"]

# creating a dataframe df
df = spark.createDataFrame(data, columns)

# show df
df.show()

# counting the total number of values in df
print("Total number of records in df:", df.count())
