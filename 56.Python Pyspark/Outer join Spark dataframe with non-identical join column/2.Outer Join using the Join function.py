# Outer Join operation
df3 = df1.join(df2, "Name", how='outer')

df3.show()
