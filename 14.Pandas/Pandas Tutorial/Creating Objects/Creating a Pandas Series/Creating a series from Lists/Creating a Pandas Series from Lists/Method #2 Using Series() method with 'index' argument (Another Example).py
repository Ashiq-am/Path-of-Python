# import pandas lib. as pd
import pandas as pd

ind = [10, 20, 30, 40, 50, 60, 70]

lst = ['Geeks', 'for', 'Geeks', 'is',
       'portal', 'for', 'geeks']

# create Pandas Series with define indexes
x = pd.Series(lst, index=ind)

# print the Series
print(x)
