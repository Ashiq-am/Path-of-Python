# if thresh value is not
# satisfied then dropping
# that row
df = df.dropna(thresh=2)
df.show()
