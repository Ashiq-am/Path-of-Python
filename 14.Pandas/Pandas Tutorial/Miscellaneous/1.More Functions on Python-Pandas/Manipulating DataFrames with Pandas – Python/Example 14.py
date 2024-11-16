# Printing five rows with name column only
# i.e. printing first 5 student names.
print(student.loc[0:4, 'Name'])

# Printing all the rows with score column
# only i.e. printing score of all the
# students
print(student.loc[:, 'Score'])

# Printing only first rows having name,
# score columns i.e. print first student
# name & their score.
print(student.iloc[0, 0:2])

# Printing first 3 rows having name,score &
# percentage columns i.e. printing first three
# student name,score & percentage.
print(student.iloc[0:3, 0:3])

# Printing all rows having name & score
# columns i.e. printing all student
# name & their score.
print(student.iloc[:, 0:2])
