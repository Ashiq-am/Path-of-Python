# Python program to sort an array of a complex
# data type in Spark using expr() function
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Create a Spark Session
spark=SparkSession.builder.getOrCreate()

# Create an array
data = [
	[3, 'A', [["Ishita", 7], ["Ashish", 9], ["Ramesh", 10], ["Mathew", 8]]],
	[7, 'D', [["Vinayak", 13], ["Pranjal", 14], ["Isha", 12], ["Adarsh", 11]]],
]

# Create a Spark data frame
df = spark.createDataFrame(
	data, "class:int, section:string, name_age:array<struct<name:string, age:int>>"
)

# Sort the name_age column by age in descending order
df = df.withColumn(
	"name_age",
	expr(
		"reverse(array_sort(transform(name_age,x->struct(x['age'] as age,x['name'] as name))))"
	),
)

# Display the data frame
df.show(2,False)
