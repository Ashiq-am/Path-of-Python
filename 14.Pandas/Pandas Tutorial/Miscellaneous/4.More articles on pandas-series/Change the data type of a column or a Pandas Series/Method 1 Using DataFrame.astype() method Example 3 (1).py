# convert data type of grade column
# into integer
df.grade = df.grade.astype(int)

# show the dataframe
print(df)

# show the datatypes
print(df.dtypes)
