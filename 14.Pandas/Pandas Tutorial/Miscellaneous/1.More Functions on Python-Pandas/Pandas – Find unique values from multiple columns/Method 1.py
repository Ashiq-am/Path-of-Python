import pandas as pd
import numpy as np

# Creating a custom dataframe.
df = pd.DataFrame({'FirstName': ['Arun', 'Navneet', 'Shilpa',
                                 'Prateek', 'Pyare', 'Prateek'],

                   'LastName': ['Singh', 'Yadav', 'Yadav', 'Shukla',
                                'Lal', 'Mishra'],

                   'Age': [26, 25, 25, 27, 28, 30]})

# To get unqiue values in 1 series/column
print(f"Unique FN: {df['FirstName'].unique()}")

# Extending the idea from 1 column to multiple columns
print(f"Unqiue Values from 3 Columns: {pd.concat([df['FirstName'], df['LastName'], df['Age']]).unique()}")
