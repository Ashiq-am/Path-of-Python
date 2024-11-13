# if any row having any Null
# value we are dropping that
# rows
df = df.dropna(how="any")
df.show()
