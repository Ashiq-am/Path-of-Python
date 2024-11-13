# using select function applying
# explode on array column
df2 = df.select(df.Name, posexplode(df.Courses_enrolled))

# printing the schema of the df2
df2.printSchema()

# show df2
df2.show()
