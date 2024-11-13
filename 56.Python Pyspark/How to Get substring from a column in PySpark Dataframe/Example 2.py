if __name__ == "__main__":

	# Creating the new column New_Country
	# and store the substring using substr()
	df = df.withColumn("New_Country", df.Country.substr(0, 12))

	# printing Dataframe schema to get the
	# column names
	df.printSchema()

	# visualizing the datframe
	df.show(truncate=False)
