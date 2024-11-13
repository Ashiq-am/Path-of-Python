# subset or filter the data with
# multiple condition
df = df.filter((df.Gender=='Male') | (df.Percentage>90))
df.show()
