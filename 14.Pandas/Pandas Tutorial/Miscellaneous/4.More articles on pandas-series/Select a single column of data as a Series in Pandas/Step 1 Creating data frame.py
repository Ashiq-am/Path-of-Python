# importing pandas as library
import pandas as pd

# creating data frame:
df = pd.DataFrame({'name': ['Akash', 'Ayush', 'Ashish',
                            'Diksha', 'Shivani'],

                   'Age': [21, 25, 23, 22, 18],

                   'MotherTongue': ['Hindi', 'English', 'Marathi',
                                    'Bhojpuri', 'Oriya']})

print("The original data frame")
df
