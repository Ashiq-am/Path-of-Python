import pandas as pd
import numpy as np

# Creating a custom dataframe.
df = pd.DataFrame({'FirstName': ['Arun', 'Navneet', 'Shilpa',
                                 'Prateek', 'Pyare', 'Prateek'],

                   'LastName': ['Singh', 'Yadav', 'Yadav', 'Shukla',
                                'Lal', 'Mishra'],

                   'Age': [26, 25, 25, 27, 28, 30]})

print(np.unique(df[['LastName', 'FirstName']].values))

# Will throw error as Age is numerical datatype
# and LastName is str
# print(np.unique(df[['LastName','Age']].values))
