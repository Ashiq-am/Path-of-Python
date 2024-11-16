# import necessary packages
import pandas as pd

# create a dataframe
Students = pd.DataFrame({'Admission_id': ['AB101', 'AB102', 'AB103',
										'AB104', 'AB105'],
						'Student_id': ['21GFG1', '21GFG2', '21GFG3',
										'21GFG4', '21GFG5'],
						'Student_Name': ['Akhil', 'Mahesh Babu', 'Warner',
										'Virat', 'ABD'],
						'Height': [5.9, 6.2, 5.6, 5.8, 5.10]})

# setting admission id as index but temperorly
Students.set_index("Admission_id")
