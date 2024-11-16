# importing the module
import pandas as pd

# read specific columns of csv file using Pandas
df = pd.read_csv("student.csv", usecols = ['Hours','Scores','Pass'])
print(df)
