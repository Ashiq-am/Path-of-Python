# importing the module
import pandas as pd

# read specific columns of csv file using Pandas
df = pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])
print(df)
