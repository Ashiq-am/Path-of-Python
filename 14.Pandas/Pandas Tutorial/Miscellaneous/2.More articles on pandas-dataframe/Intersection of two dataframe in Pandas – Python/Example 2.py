import pandas as pd

# Creating Data frames
df1 = {'A': [1, 2, 3, 4],
       'B': ['Geeks', 'For', 'efg', 'ghi']}
df2 = {'A': [1, 2, 3, 4],
       'B': ['Geeks', 'For', 'abc', 'cde'],
       'C': ['Nikhil', 'Rishabh', 'Rahul', 'Shubham']}

d1 = pd.DataFrame(df1)
d2 = pd.DataFrame(df2)

# Calling merge() function
int_df = pd.merge(d1, d2, how='inner', on=['A', 'B'])
print(int_df)
