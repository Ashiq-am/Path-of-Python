from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Initialize Spark session
spark = SparkSession.builder.appName("PivotExample").getOrCreate()

# Sample data
data = [
    ('2024-01-01', 'ProductA', 10),
    ('2024-01-01', 'ProductB', 20),
    ('2024-01-02', 'ProductA', 30),
    ('2024-01-02', 'ProductB', 40),
]

# Create DataFrame
df = spark.createDataFrame(data, ['date', 'product', 'sales'])

df.show()

# Pivot DataFrame
pivot_df = df.groupBy('date').pivot('product').agg(sum('sales'))

print("Dataframe after Pivot Operation")
pivot_df.show()
