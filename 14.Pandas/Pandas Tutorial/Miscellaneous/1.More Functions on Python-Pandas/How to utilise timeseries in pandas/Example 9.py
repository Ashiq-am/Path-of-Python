# import packages and libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# reading the dataset
df = pd.read_csv('covid_19_data.csv', encoding='UTF-8')

# convert Last update column to datetime
df['Last Update'] = pd.to_datetime(df['Last Update'])

# setting index
df.set_index('Last Update', inplace=True)

# plotting figure
df.plot.line()
