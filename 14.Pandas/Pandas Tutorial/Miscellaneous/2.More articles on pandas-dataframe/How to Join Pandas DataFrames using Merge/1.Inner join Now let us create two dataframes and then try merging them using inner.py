import numpy as np
import pandas as pd

left = pd.DataFrame({'Sr.no': ['1', '2', '3', '4', '5'],
                     'Name': ['Rashmi', 'Arun', 'John',
                              'Kshitu', 'Bresha'],
                     'Roll No': ['1', '2', '3', '4', '5']})

right = pd.DataFrame({'Sr.no': ['2', '4', '6', '7', '8'],
                      'Gender': ['F', 'M', 'M', 'F', 'F'],
                      'Interest': ['Writing', 'Cricket', 'Dancing',
                                   'Chess', 'Sleeping']})

# Merging the dataframes
pd.merge(left, right, how='inner', on='Sr.no')
