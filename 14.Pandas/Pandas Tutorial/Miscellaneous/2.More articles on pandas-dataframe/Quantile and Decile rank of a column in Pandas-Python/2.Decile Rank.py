# importing the modules
import pandas as pd
import numpy as np

# creating a DataFrame
df = {'Name': ['Amit', 'Darren', 'Cody', 'Drew',
               'Ravi', 'Donald', 'Amy'],
      'Score': [50, 71, 87, 95, 63, 32, 80]}
df = pd.DataFrame(df, columns=['Name', 'Score'])

# adding Decile_rank column to the DataFrame
df['Decile_rank'] = pd.qcut(df['Score'], 10,
                            labels=False)

# printing the DataFrame
print(df)
