# if the subset column any value
# is NULL then dropping that row
df = df.dropna(subset="City")
df.show()
