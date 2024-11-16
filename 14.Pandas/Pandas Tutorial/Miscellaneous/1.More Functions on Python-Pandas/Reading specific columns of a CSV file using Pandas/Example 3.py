# importing the module
import pandas as pd

# read specific columns of csv file using Pandas
df = pd.read_csv("titanic.csv", usecols = ['Survived','Pclass'])
print(df)
