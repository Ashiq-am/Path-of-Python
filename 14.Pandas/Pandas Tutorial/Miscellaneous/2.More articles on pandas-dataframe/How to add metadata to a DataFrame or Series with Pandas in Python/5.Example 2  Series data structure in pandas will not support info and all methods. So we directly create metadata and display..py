# import required module
import pandas as pd

# intialise data of lists using dictionary.
data = {'Name': ['Sravan', 'Deepak', 'Radha', 'Vani'],
		'College': ['vignan', 'vignan Lara', 'vignan', 'vignan'],
		'Department': ['CSE', 'IT', 'IT', 'CSE'],
		'Profession': ['Student', 'Assistant Professor',
					'Programmer & ass. Proff',
					'Programmer & Scholar'],
		'Age': [22, 32, 45, 37]
		}

# Create series
ser = pd.Series(data)

# display data
ser
