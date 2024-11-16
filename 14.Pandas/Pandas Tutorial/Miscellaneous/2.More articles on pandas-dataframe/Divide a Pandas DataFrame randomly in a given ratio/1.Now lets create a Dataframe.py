# Importing required libraries
import pandas as pd

record = {
	'course_name': ['Data Structures', 'Python',
					'Machine Learning', 'Web Development'],
	'student_name': ['Ankit', 'Shivangi',
					'Priya', 'Shaurya'],
	'student_city': ['Chennai', 'Pune',
					'Delhi', 'Mumbai'],
	'student_gender': ['M', 'F',
					'F', 'M'] }

# Creating a dataframe
df = pd.DataFrame(record)

# show the dataframe
df
