# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# To find the correlation among
# the columns using kendall method
df.corr(method ='kendall')
