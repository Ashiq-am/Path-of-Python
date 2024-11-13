# now using select function applying
# explode_outer on array column
df4 = df.select(df.Name, explode_outer(df.Courses_enrolled))

# printing the schema of the df4
df4.printSchema()

# show df2
df4.show()
