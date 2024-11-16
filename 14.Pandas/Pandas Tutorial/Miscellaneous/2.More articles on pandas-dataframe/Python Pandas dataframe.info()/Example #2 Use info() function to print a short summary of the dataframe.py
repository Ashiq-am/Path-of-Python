# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# Print the short summary of the
# dataframe by setting verbose = False
df.info(verbose = False)
