# creating the row data for dataframe
data = [('Jaya', 'Sinha', 'F', '1991-04-01'),
		('Milan', 'Sharma', '', '2000-05-19'),
		('Rohit', 'Verma', 'M', '1978-09-05'),
		('Maria', 'Anne', 'F', '1967-12-01'),
		('Jay', 'Mehta', 'M', '1980-02-17')
		]

# giving the column names for the dataframe
columns = ['First Name', 'Last Name', 'DOB']

# creating the dataframe df
df = spark.createDataFrame(data, columns)

# printing dataframe schema
df.printSchema()

# show dataframe
df.show()

# defining split ()
split_cols = pyspark.sql.functions.split(df['DOB'], '-')

# applying split() using select()
df3 = df.select('First Name', 'Last Name', 'Gender', 'DOB',
				split_cols.getItem(0).alias('year'),
				split_cols.getItem(1).alias('month'),
				split_cols.getItem(2).alias('day'))

# show df3
df3.show()
