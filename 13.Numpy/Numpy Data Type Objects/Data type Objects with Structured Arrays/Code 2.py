# Python program to demonstrate
# the use of data type object
# with structured array.
import numpy as np

dt = np.dtype([('name', np.unicode_, 16),
               ('grades', np.float64, (2,))])

# x is a structured array with names
# and marks of students.
# Data type of name of the student is
# np.unicode_ and data type of marks is
# np.float(64)
x = np.array([('Sarah', (8.0, 7.0)),
              ('John', (6.0, 7.0))], dtype=dt)

print(x[1])

print("Grades of John are: ", x[1]['grades'])
print("Names are: ", x['name'])