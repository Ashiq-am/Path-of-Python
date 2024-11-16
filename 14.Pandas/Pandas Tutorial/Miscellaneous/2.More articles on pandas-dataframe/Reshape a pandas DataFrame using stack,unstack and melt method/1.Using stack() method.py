# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("nba.csv")

# reshape the dataframe using stack() method
df_stacked = df.stack()

print(df_stacked.head(26))
