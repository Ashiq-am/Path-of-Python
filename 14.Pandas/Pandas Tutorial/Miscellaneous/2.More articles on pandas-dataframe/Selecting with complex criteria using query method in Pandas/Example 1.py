import pandas as pd

df = pd.DataFrame([[10, 20, 30, 40], [70, 14, 21, 80],
                   [55, 15, 80, 12]],

                  columns=['GFG_USER_1', 'GFG_USER_2',
                           'GFG_USER_3', 'GFG_USER_4'],

                  index=['Practice1', 'Practice2', 'Practice3'])

print(df, "\n")

# Filter data using query method
df1 = df.loc[df.query(
    'GFG_USER_1 <= 80 & GFG_USER_2 > 10 & \
GFG_USER_3 < 50 & GFG_USER_4 == 80').index]

print(df1)
