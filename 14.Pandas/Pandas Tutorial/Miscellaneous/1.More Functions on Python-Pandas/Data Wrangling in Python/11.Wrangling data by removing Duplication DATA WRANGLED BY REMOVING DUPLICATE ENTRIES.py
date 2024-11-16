# import module
import pandas as pd

# initializing Data
student_data = {'Name': ['Amit', 'Praveen', 'Jagroop',
						'Rahul', 'Vishal', 'Suraj',
						'Rishab', 'Satyapal', 'Amit',
						'Rahul', 'Praveen', 'Amit'],

				'Roll_no': [23, 54, 29, 36, 59, 38,
							12, 45, 34, 36, 54, 23],
				'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com',
						'xxxxxx@gmail.com', 'xx@gmail.com',
						'xxxx@gmail.com', 'xxxxx@gmail.com',
						'xxxxx@gmail.com', 'xxxxx@gmail.com',
						'xxxxx@gmail.com', 'xxxxxx@gmail.com',
						'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

# creating dataframe
df = pd.DataFrame(student_data)

# Here df.duplicated() list duplicate Entries in ROllno.
# So that ~(NOT) is placed in order to get non duplicate values.
non_duplicate = df[~df.duplicated('Roll_no')]

# printing non-duplicate values
print(non_duplicate)
