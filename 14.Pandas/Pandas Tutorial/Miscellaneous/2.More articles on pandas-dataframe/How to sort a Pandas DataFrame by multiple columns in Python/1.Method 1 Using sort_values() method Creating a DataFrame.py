#import libraries
import numpy as np
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'Name': ['Raj', 'Akhil', 'Sonum', 'Tilak', 'Divya', 'Megha'],
				'Age': [20, 22, 21, 19, 17, 23],
				'Rank': [1, np.nan, 8, 9, 4, np.nan]})

# printing the dataframe
print('DATAFRAME')
df
