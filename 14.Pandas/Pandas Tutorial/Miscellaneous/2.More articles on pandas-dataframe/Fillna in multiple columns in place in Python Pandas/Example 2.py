# Importing Required Libraries
import pandas as pd
import numpy as np

# Creating a sample dataframe with NaN values
dataframe = pd.DataFrame({'Count': [1, np.nan, np.nan, 4, 2,
                                    np.nan, np.nan, 5, 6],

                          'Name': ['Geeks', 'for', 'Geeks', 'a', 'portal', 'for',
                                   'computer', 'Science', 'Geeks'],
                          'Category': list('ppqqrrsss')})

# Filling Count column with mean of Count column
dataframe.fillna(dataframe['Count'].mean(), inplace=True)

# Printing the Dataframe
display(dataframe)
