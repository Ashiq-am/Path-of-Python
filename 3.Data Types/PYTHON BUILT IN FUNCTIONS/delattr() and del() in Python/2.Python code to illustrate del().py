# Python code to illustrate del()
class Geek:
    stu1 = "Henry"
    stu2 = "Zack"
    stu3 = "Stephen"
    stu4 = "Amy"
    stu5 = "Shawn"

names = Geek()

print('Students before del--')
print('First = ',names.stu1)
print('Second = ',names.stu2)
print('Third = ',names.stu3)
print('Fourth = ',names.stu4)
print('Fifth = ',names.stu5)

# implementing the operator
del Geek.stu5

print('After deleting fith student--')
print('First = ',names.stu1)
print('Second = ',names.stu2)
print('Third = ',names.stu3)
print('Fourth = ',names.stu4)
# this statement raises an error
print('Fifth = ',names.stu5)
