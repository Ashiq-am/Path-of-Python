# importing Pandas library
import pandas as pd

pd.read_csv(filepath_or_buffer="pokemon.csv")

# makes the passed rows header
pd.read_csv("pokemon.csv", header=[1, 2])

# make the passed column as index instead of 0, 1, 2, 3....
pd.read_csv("pokemon.csv", index_col='Type')

# uses passed cols only for data frame
pd.read_csv("pokemon.csv", usecols=["Type"])

# reutruns pandas series if there is only one colunmn
pd.read_csv("pokemon.csv", usecols=["Type"],
            squeeze=True)

# skips the passed rows in new series
pd.read_csv("pokemon.csv",
            skiprows=[1, 2, 3, 4])
