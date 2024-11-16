import pandas as pd

df = pd.DataFrame([[100, 200, 300], [70, 140, 210],
                   [55, 150, 180]],

                  columns=['PAK', 'AUS', 'IND'],

                  index=['Match1', 'Match2', 'Match3'])

print(df, "\n")

# Filter data using query method
df1 = df.loc[df.query('PAK <= 80 & AUS > 100 & IND < 250').index]

print(df1)
