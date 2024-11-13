# Create a DataFrame from the Row object and the schema
df = spark.createDataFrame(data, schema=schema)
# Show the DataFrame
df.show()
