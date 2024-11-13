import pandas as pd

print('Read data...')

# enter the complete path of the csv file
df = pd.read_csv('../price.csv',header=0).head(1000)
data = df.values
