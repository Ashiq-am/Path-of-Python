# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# column index value of "Name" column is 0
# We have set takeable = True
# to interpret the index / col as indexer
df.get_value(4, 0, takeable = True)
