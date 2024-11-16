# Import Necessary Libraries
import pandas as pd
import numpy as np

# Creating a DataFrame with
# random values
df = pd.DataFrame({'Alphabet': ['a', 'b', 'c', 'c',
                                'a', 'a', 'c', 'b'],

                   'Frequency': [-10, 29, -12, -190,
                                 72, -98, -12, 0],

                   'BandWidth': [10, 34, 23, -10, -87,
                                 -76, 365, 10]})

print(df)

# Group By dataframe on categorical
# values
d = df.groupby(df['Alphabet'])


# creating lambda function to calculate
# positive as well as negative values
def pos(col):
    return col[col > 0].sum()


def neg(col):
    return col[col < 0].sum()


# Apply lambda function to particular
# column
print(d['Frequency'].agg([('negative_values', neg),
                          ('positive_values', pos)
                          ]))

print(d['Bandwidth'].agg([('negative_values', neg),
                          ('positive_values', pos)
                          ]))
