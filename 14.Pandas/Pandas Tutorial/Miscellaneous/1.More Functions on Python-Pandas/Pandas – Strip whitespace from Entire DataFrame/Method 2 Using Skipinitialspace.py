# importing library
import pandas as pd

# reading csv file and at a same time using skipinitial attribute which will remobe extra space
df = pd.read_csv('\\student_data.csv', skipinitialspace = True)

# printing dataset
print(df)
