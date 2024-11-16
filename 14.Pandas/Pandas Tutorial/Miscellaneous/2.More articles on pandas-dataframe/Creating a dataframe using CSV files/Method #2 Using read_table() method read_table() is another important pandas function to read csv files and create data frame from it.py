# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd

# creating a data frame
df = pd.read_table("CardioGoodFitness.csv", delimiter =", ")
print(df.head())
