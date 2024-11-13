data = [('Rahul', 25), ('Aman', 30), ('Ravi', 28)]
columns = ['Name', 'Age']

df = spark.createDataFrame(data, columns)
df.show()
