# importing pandas module
import pandas as pd

# reading csv file
data = pd.read_csv("pokemon.csv")

# displying dataframe - Output 1
data.head()

# inserting column with static value in data frame
data.insert(2, "Team", "Any")

# displaying data frame again - Output 2
data.head()
