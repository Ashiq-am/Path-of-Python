# import packages
import pandas as pd

# read csv file
df = pd.read_csv('covid_19.csv')
df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df['Last Update'] = pd.to_datetime(df['Last Update'])
df = df.set_index('ObservationDate')

# observations taken from may 20th to may 21st of 2021
df.loc['2021-05-20':'2021-05-21']
