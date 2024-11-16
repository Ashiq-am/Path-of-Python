# import required modules
import pandas as pd
import numpy as np

# create dataset
df = pd.DataFrame({'A': ['hello', 'vignan', 'geeks'],
				'B': ['vignan', 'hello', 'hello'],
				'C': [1, 2, 3]})

# display dataset
print(df)

# create dymmy variables
pd.get_dummies(df)
