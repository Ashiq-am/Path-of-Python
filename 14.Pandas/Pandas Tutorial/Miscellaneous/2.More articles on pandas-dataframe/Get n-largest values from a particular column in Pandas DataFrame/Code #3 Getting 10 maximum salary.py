# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# five largest values in column Salary
df.nlargest(5, ['Salary'])
