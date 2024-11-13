if __name__ == "__main__":

	# creating Month column and get the
	# substring from the Data column
	# creating Date column and get the
	# substring from the Data column
	df = df.withColumn(
	"Month", substring("Data", 1, 2)).withColumn(
	"Date", substring("Data", 3, 4))

	# dropping the Data column from the
	# Dataframe
	df = df.drop("Data")

	# printing Dataframe schema to get the
	# column names
	df.printSchema()

	# visualizing the datframe
	df.show(truncate=False)
