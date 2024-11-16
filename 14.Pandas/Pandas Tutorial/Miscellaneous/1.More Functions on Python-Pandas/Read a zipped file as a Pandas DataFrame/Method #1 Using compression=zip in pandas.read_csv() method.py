# import required modules
import zipfile
import pandas as pd

# read the dataset using the compression zip
df = pd.read_csv('test.zip',compression='zip')

# display dataset
print(df.head())
