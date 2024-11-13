# import necessary packages
import pandas as pd

# create dataframe
students = pd.DataFrame({'student_ID': [101, 102, 103],
						'student_Name': ['Hary', 'Ron', 'Alexa'],
						'Branch': ['CSE', 'ECE', 'CSE'],
						'Marks': [87, 88, 72]})
# Table
print(students)

# mean values for all numeric columns
print(students.mean())
