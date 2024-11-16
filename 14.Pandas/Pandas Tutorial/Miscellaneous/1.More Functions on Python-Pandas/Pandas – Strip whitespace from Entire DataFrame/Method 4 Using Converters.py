# importing library
import pandas as pd

# reading csv file and at a same time using converters attribute which will remove extra space
df = pd.read_csv('\\student_data.csv', converters={'Name': str.strip(),
												'Blood Group' : str.strip(),
												'Gender' : str.strip() } )

# printing dataset
print(df)
