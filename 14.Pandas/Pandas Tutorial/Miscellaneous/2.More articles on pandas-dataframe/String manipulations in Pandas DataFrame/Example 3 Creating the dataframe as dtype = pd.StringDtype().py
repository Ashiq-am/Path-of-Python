# now creating the dataframe as dtype = pd.StringDtype()
import pandas as pd
import numpy as np

df = pd.Series(['Gulshan', 'Shashank', 'Bablu', 'Abhishek',
				'Anand', np.nan, 'Pratap'], dtype=pd.StringDtype())

print(df)
