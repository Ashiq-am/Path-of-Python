# import module
import pandas as pd

# creating DataFrame for Student Details
details = pd.DataFrame({
	'ID': [101, 102, 103, 104, 105, 106,
		107, 108, 109, 110],
	'NAME': ['Jagroop', 'Praveen', 'Harjot',
			'Pooja', 'Rahul', 'Nikita',
			'Saurabh', 'Ayush', 'Dolly', "Mohit"],
	'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE',
			'CSE', 'CSE', 'CSE', 'CSE', 'CSE']})

# printing details
print(details)
