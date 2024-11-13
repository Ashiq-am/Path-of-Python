# Create data in dataframe
data2 = [(('Mohi'), '1991-04-01', 'M', 3000),
		(('Ani'), '2000-05-19', 'F', 4300),
		(('Shipta'), '1978-09-05', 'F', 4200),
		(('Jessy'), '1967-12-01', 'F', 4010),
		(('kanne'), '1980-02-17', 'F', 1200)]

# Column names in dataframe
columns = ["Name", "DOB", "Gender", "salary"]

# Create the spark dataframe
df2 = spark.createDataFrame(data=data, schema=columns)

# Print the dataframe
df2.show()
