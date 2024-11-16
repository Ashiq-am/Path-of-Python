import pandas as pd
import numpy as np

# Creating a custom dataframe.
df = pd.DataFrame({'FirstName': ['Arun', 'Navneet', 'Shilpa',
                                 'Prateek', 'Pyare', 'Prateek'],

                   'LastName': ['Singh', 'Yadav', 'Yadav', 'Shukla',
                                'Lal', 'Mishra'],

                   'Age': [26, 25, 25, 27, 28, 30]})

# Typecasting pandas series into set and then
# taking set union (|)
print(set(df.FirstName) | set(df.LastName) | set(df.Age))
