import pandas as pd

df = pd.DataFrame([[1000, 2000, 3000, 4000], [7000, 1400, 2100, 2800],
                   [5500, 1500, 800, 1200]],

                  columns=['DSA_Self_Paced', 'OOPS', 'DBMS', 'System_design'],

                  index=['Sale1', 'Sale2', 'Sale3'])

print(df, "\n")

# Filter data using query method
df1 = df.loc[df.query(
    'DSA_Self_Paced <= 6000 & OOPS > 1400 & DBMS < 1500 \
    & System_design == 1200').index]

print(df1)
