# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# Print the full summary of the dataframe
# with null count excluded
df.info(verbose = True, null_counts = False)
