# import pandas library
import pandas as pd

# create a Dataframe
data = pd.DataFrame({
	'course_name': ['Data Structures', 'Python',
					'Machine Learning'],
	'student_name': ['A', 'B',
					'C'],
	'student_city': ['Chennai', 'Pune',
					'Delhi'],
	'student_gender': ['M', 'F',
					'M'] })
# show the Dataframe
data
