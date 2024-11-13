# Order the data by ascending order
# of Salary
df.orderBy(['Salary'], ascending = [True]).show()

# or
# df.orderBy(f.col("Salary").asc()).show()

# or
# df.orderBy(['Salary']).show()
