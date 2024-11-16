# Importing Required Libraries
import pandas as pd
import numpy as np

# Creating a sample dataframe with NaN values
dataframe = pd.DataFrame({'Count': [1, np.nan, np.nan, 4, 2,
                                    np.nan, np.nan, 5, 6],

                          'Name': ['Geeks', 'for', 'Geeks', 'a', 'portal', 'for',
                                   'computer', 'Science', 'Geeks'],
                          'Category': list('ppqqrrsss')})

# Creating a constant value for coloumn Count
constant_values = {'Count': 10}
dataframe = dataframe.fillna(value=constant_values)

# Printing the dataframe
display(dataframe)
