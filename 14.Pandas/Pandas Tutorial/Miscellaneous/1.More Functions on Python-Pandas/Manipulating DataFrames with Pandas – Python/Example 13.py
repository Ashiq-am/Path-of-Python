# Selecting rows where score is
# greater than 70
print(student[student.Score>70])

# Selecting rows where score is greater than 60
# OR less than 70
print(student[(student.Score>60) | (student.Score<70)])
