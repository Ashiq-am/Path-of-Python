# import packages
import pandas as pd

# create data
df = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12,
                          3: 13, 4: 67, 5: 89,
                          6: 90, 7: 56, 8: 34},

                   'Name': {0: 'Ram', 1: 'Deep', 2: 'Yash',
                            3: 'Aman', 4: 'Arjun', 5: 'Aditya',
                            6: 'Akash', 7: 'Chalsea',
                            8: 'Divya'},

                   'Marks': {0: 89, 1: 97, 2: 45,
                             3: 78, 4: 56, 5: 76,
                             6: 81, 7: 87, 8: 100},

                   'Grade': {0: 'B', 1: 'A', 2: 'F',
                             3: 'C', 4: 'E', 5: 'C',
                             6: 'B', 7: 'B', 8: 'A'}})

# view data
display(df)
