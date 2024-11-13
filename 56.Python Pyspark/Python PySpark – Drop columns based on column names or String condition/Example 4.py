df = spark.read.csv('book1.csv', header=True, inferSchema=True)
df.show()
