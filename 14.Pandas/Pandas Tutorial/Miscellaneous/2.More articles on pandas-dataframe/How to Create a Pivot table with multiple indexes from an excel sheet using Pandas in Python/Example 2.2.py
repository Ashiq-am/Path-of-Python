# importing pandas as pd
import pandas as pd

# Create the dataframe
df=pd.read_csv('dataset/new_players.csv')

# Print the resultant table
print(pd.pivot_table(df,index=["century","name"]))
