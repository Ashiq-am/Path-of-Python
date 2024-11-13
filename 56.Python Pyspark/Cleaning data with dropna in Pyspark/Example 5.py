# if thresh value is satisfied with subset
# column then dropping that row
df = df.dropna(thresh=2,subset=("Id","Name","City"))
df.show()
