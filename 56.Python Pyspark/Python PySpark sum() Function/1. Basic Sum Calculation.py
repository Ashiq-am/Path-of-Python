from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create a Spark session
spark = SparkSession.builder.appName("SumExample").getOrCreate()

# Sample data
data = [
    ("Science", 93),
    ("Physics", 72),
    ("Operation System", 81)
]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Marks"])

# Show the DataFrame
df.show()

# Calculate the sum of the 'Marks' column
total_marks = df.select(sum("Marks")).collect()[0][0]
print(f"Total Marks: {total_marks}")
