# importing pandas as pd
import pandas as pd

# Create the dataframe
df=pd.read_csv('GeeksForGeeks.csv')

# Print the resultant table
print(pd.pivot_table(df,index=["Country"]))
