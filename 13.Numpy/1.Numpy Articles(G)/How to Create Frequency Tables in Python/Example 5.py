# import packages
import pandas as pd
import numpy as np

# reading csv file
data = pd.read_csv('SampleSuperstore.csv')

# two way frequency table for the ship mode column
# and consumer column of the superstore dataset.
freq_table = pd.crosstab(data['Ship Mode'], data['Segment'])

freq_table
