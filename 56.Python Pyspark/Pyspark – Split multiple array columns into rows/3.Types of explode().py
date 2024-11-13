# creating the row data and giving array
# values for dataframe along with null values
data = [('Jaya', '20', ['SQL', 'Data Science']),
		('Milan', '21', ['ML', 'AI']),
		('Rohit', '19', None),
		('Maria', '20', ['DBMS', 'Networking']),
		('Jay', '22', None)]

# column names for dataframe
columns = ['Name', 'Age', 'Courses_enrolled']

# creating dataframe with createDataFrame()
df = spark.createDataFrame(data, columns)

# printing dataframe schema
df.printSchema()

# show dataframe
df.show()
