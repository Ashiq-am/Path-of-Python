# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("nba.csv")

# it takes two columns "Name" and "Team"
df_melt = df.melt(id_vars =['Name', 'Team'])
print(df_melt.head(10))
