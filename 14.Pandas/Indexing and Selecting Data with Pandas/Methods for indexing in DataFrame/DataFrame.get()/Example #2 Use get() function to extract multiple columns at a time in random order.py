# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

df.get(["Salary", "Team", "Name"])
