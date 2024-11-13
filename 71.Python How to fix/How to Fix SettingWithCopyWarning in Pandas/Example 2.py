# import necessary packages
import pandas as pd

# create a dataframe
marks = pd.DataFrame({'Name': ['Akhil', 'Sai', 'Rohit', 'Prasanth', 'Divya'],
					'Percentage': ['-', '-', 90, 79, 89],
					'Grade': ['-', '-', 'O', 'B', 'A']})

# create a copy of orginal DataFrame whose
percentage is empty(absenties)
Absent_Students = marks.loc[marks.Percentage == '-', :].copy()

# Make their grade as 'Ab' which indicates absent.
Absent_Students.Grade = 'Ab'

# modified content
Absent_Students
