#CSV file can be downloaded from the link mentioned above.
data = spark.read.csv('book_ratings.csv',
					inferSchema=True,header=True)

data.show(5)
