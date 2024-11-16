# import packages
import pandas as pd

# read csv file
df = pd.read_csv('covid_19.csv')
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df['Last Update'] = pd.to_datetime(df['Last Update'])
df = df.set_index('ObservationDate')
print(df.groupby(level=0).count())
