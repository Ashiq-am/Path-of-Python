# importing sparksession from pyspark.sql mudule
from pyspark.sql import SparkSession

# creating sparksession and giving app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

# giving rows value for dataframe
data = [("Ram", "IT", 44, 80000),
		("Shyam", "Sales", 45, 70000),
		("Jiya", "Sales", 30, 60000),
		("Maria", "Accounts", 29, 65000),
		("Ram", "IT", 38, 80000),
		("John", "Management", 35, 80000),
		("Shyam", "Sales", 45, 70000),
		("Kumar", "Sales", 27, 70000),
		("Maria", "Accounts", 32, 65000),
		("Ria", "Management", 32, 65000)]

# giving column names of dataframe
columns = ["Emp_name", "Depart", "Age", "Salary"]

# creating a dataframe df
df = spark.createDataFrame(data, columns)

# show df
df.show()

# counting the total number of values in df
print("Total number of records in df:", df.count())
