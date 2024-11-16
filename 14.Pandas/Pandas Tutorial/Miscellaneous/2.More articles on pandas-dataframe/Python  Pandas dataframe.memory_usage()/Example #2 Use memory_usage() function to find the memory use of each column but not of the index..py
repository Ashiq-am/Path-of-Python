# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# Function to find memory use of each
# column but not of the index
# we set index = False
df.memory_usage(index = False)
