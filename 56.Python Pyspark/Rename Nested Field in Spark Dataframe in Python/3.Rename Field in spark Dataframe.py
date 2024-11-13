df2 = (df.withColumnRenamed("fname","FirstName")
	.withColumnRenamed("lname","LastName")
	)
df2.printSchema()
