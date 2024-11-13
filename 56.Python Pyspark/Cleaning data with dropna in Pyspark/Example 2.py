# if any row having all Null
# values we are dropping that
# rows.
df = df.dropna(how="all")
df.show()
