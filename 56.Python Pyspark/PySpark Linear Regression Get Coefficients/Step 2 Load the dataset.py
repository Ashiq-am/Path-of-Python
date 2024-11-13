# Reading the data
df = spark.read.csv('Ecommerce_Customers.csv',inferSchema=True, header=True)

# Showing the data
df.show(5)
