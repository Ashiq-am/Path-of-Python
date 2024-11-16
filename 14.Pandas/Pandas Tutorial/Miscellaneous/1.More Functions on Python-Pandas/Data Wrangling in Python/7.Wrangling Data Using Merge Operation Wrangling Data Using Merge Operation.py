# Import module
import pandas as pd

# Creating Dataframe
details = pd.DataFrame({
	'ID': [101, 102, 103, 104, 105,
		106, 107, 108, 109, 110],
	'NAME': ['Jagroop', 'Praveen', 'Harjot',
			'Pooja', 'Rahul', 'Nikita',
			'Saurabh', 'Ayush', 'Dolly', "Mohit"],
	'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE',
			'CSE', 'CSE', 'CSE', 'CSE', 'CSE']})

# Creating Dataframe
fees_status = pd.DataFrame(
	{'ID': [101, 102, 103, 104, 105,
			106, 107, 108, 109, 110],
	'PENDING': ['5000', '250', 'NIL',
				'9000', '15000', 'NIL',
				'4500', '1800', '250', 'NIL']})

# Merging Dataframe
print(pd.merge(details, fees_status, on='ID'))
