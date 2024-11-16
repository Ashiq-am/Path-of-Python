# importing packages
import pandas as pd

# importing 'train.csv'
data = pd.read_csv('train.csv')
pd.set_option('display.max_columns', 4)
data.head()
