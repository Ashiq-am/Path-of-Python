if __name__ == "__main__":

	input_data = [("India", +91, "AidanButler"),
				("United States of America", +1, "ConerFlores"),
				("Israel", +972, "RosseBryant"),
				("Dubai", +971, "JuliaSimmon"),
				("Russia", 7, "AliceBailey")]

	# calling function to create SparkSession
	spark = create_session()

	schema = ["Country", "Country Code", "Name"]

	# calling function to create dataframe
	df = create_df(spark, input_data, schema)

	# Selecting the column using selectExpr()
	# function and getting susbtring using substring()
	df2 = df.selectExpr('Name', 'substring(Name, 1,5) as First_Name',
						'substring(Name, 6,6) as Last_Name')

	# printing Dataframe schema to get the column names
	df2.printSchema()

	# visualizing the datframe
	df2.show(truncate=False)
