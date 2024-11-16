# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# will replace Nan value in dataframe with value -99999
df.replace(to_replace = pd.np.nan, value =-99999)
