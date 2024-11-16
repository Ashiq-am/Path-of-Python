# find the column name of maximum
# values in every row
maxValueIndex = df.idxmax(axis = 1)

print("Max values of row are at following columns :")
print(maxValueIndex)
