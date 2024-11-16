import pandas as pd

url = 'http://bit.ly/uforeports'

# read csv file
df = pd.read_csv(url)
df.head()
