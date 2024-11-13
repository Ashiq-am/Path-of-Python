# import necessary packages
import pandas as pd

# create a dataframe
marks = pd.DataFrame({'Name': ['Akhil', 'Sai', 'Rohit', 'Prasanth', 'Divya'],
					'Percentage': ['-', 65, 90, 79, 89],
					'Grade': ['-', 'C', 'O', 'B', 'A']})

# Assign Absent if percentage is not specified
marks[marks.Percentage == '-'].Grade = 'Ab'
