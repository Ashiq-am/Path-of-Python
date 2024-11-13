# Sample data
data = [
    (1, 1101),
    (2, 1102),
    (3, 1101),
    (4, 1102)
]

# Column names
columns = ["customer_id", "trigger_id"]

# Create DataFrame
df = spark.createDataFrame(data, columns)
df.show()
