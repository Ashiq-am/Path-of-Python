# import packages
import pandas as pd

# read csv file
df = pd.read_csv('covid_19.csv', encoding='UTF-8')

df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
df['Last Update'] = pd.to_datetime(df['Last Update'])
print(df)
