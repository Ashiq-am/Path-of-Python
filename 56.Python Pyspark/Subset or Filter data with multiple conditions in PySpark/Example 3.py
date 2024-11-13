# subset or filter the dataframe by
# passing Multiple condition
df = df.filter((df.Gender=='Female') & (df.Age>=18))
df.show()
