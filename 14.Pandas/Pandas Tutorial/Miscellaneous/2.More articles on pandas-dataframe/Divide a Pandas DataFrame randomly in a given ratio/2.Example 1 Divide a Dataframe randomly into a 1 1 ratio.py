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

# Creating a dataframe with 50%
# values of original dataframe
part_50 = df.sample(frac = 0.5)

# Creating dataframe with
# rest of the 50% values
rest_part_50 = df.drop(part_50.index)

print("\n50% of the givem DataFrame:")
print(part_50)

print("\nrest 50% of the given DataFrame:")
print(rest_part_50)
