from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("PySpark Pivot Example").getOrCreate()

# Sample data
data = [
    ("A", "East", 100),
    ("A", "West", 150),
    ("B", "East", 200),
    ("B", "West", 250),
    ("C", "East", 300),
    ("C", "West", 350)
]

# Create a DataFrame
columns = ["Product", "Region", "Sales"]
df = spark.createDataFrame(data, columns)

# Show the initial DataFrame
df.show()
