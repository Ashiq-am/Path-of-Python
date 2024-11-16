# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("nba.csv")

# unstack() method
df_unstacked = df_stacked.unstack()
print(df_unstacked.head(10))
