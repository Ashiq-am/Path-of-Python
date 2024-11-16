# now creating the dataframe as dtype = 'string'
import pandas as pd
import numpy as np

df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek',
				'Anand', np.nan, 'Pratap'], dtype='string')

print(df)
