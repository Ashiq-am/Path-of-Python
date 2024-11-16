# Import module
import pandas as pd

# Initializing Data
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

# Creating Dataframe of Data
df = pd.DataFrame(student_data)

# Printing Dataframe
print(df)
