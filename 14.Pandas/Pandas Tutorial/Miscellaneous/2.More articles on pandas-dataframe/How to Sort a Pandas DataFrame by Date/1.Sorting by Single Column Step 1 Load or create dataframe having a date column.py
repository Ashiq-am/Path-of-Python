# importing package
import pandas as pd

# Creating a dataframe that stores records of students taking admission in a college
data = pd.DataFrame({'AdmissionDate': ['2021-01-25','2021-01-22','2021-01-20',
						'2021-01-18','2021-01-22','2021-01-17','2021-01-21'],
					'StudentID': [7,5,3,2,6,1,4],
					'Name': ['Ram','Shyam','Mohan','Sohan','Lucky','Abhinav','Danny'],
					'Stream':['CSE','ECE','Civil','Mechanical','CSE','IT','EEE']
				})
# Checking dataframe
print(data)
