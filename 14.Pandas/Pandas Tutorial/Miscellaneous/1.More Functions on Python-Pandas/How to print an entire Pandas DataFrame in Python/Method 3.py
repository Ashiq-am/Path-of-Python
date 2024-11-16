import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data.data,
				columns = data.feature_names)

# Permanently changes the pandas settings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

# All dataframes hereafter reflect these changes.
display(df)

print('**RESET_OPTIONS**')

# Resets the options
pd.reset_option('all')
display(df)
