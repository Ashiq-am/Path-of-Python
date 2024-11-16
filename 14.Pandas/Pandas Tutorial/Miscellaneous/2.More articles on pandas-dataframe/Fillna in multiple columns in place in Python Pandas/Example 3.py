# Importing Required Libraries
import pandas as pd
import numpy as np

# Creating a sample dataframe with NaN values
dataframe = pd.DataFrame({'Count': [1, np.nan, np.nan,
                                    1, 2, np.nan, np.nan,
                                    5, 1],

                          'Name': ['Geeks', 'for', 'Geeks', 'a', 'portal', 'for',
                                   'computer', 'Science', 'Geeks'],
                          'Category': list('ppqqrrsss')})

# Using Mode() function to impute the values using fillna
dataframe.fillna(dataframe['Count'].mode()[0], inplace=True)

# Printing the Dataframe
display(dataframe)
