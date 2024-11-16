# importing pandas
import pandas as pd

# multi-list
list = [['Geeks'], ['For'], ['Geeks'], ['is'],
        ['a'], ['portal'], ['for'], ['geeks']]

# create Pandas Series
df = pd.Series((i[0] for i in list))

print(df)
