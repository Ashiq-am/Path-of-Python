# Import Necessary Libraries
import pandas as pd
import numpy as np

# Creating a DataFrame with random values
df = pd.DataFrame({'Function': ['F(x)', 'F(x)', 'F(y)',
                                'F(x)', 'F(y)', 'F(x)',
                                'F(x)', 'F(y)'],

                   'X': [-10, 29, -12, -190, 72, -98,
                         -12, 0],

                   'Y': [10, 34, 23, -10, -87, -76,
                         365, 10]})

print(df)

# Group By dataframe on categorical values
d = df.groupby(df['Function'])


# creating lambda function to calculate
# positive as well as negative values
def pos(col):
    return col[col > 0].sum()


def neg(col):
    return col[col < 0].sum()


# Apply lambda function to particular
# column
print(d['X'].agg([('negative_values', neg),
                  ('positive_values', pos)
                  ]))

print(d['Y'].agg([('negative_values', neg),
                  ('positive_values', pos)
                  ]))
