# import library
import pandas as pd

# create a Dataframe
df = pd.DataFrame({
    'height': [165, 165, 164,
               158, 167, 160,
               158, 165],

    'weight': [63.5, 64, 63.5,
               54, 63.5, 62,
               64, 64],

    'age': [20, 22, 22,
            21, 23, 22,
            20, 21]},

    index=['Steve', 'Ria', 'Nivi',
           'Jane', 'Kate', 'Lucy',
           'Ram', 'Niki'])

# show the Dataframe
df
