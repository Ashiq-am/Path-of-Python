# import necessary packages
import numpy as np

# create a 2D Array
students = np.array([['Student ID', 'Student Name', 'Branch', 'Marks'],
					[101, 'Hary', 'CSE', 87],
					[102, 'Ron', 'ECE', 88],
					[103, 'Alexa', 'CSE', 72]])

# mean of marks(3rd column)
print(students[:, 3].mean())
