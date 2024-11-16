# import packages
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
matplotlib
inline

# reading csv file as pandas dataframe
data = pd.read_csv('iris.csv')

# one way frequency table for the species column.
freq_table = pd.crosstab(data['species'], 'no_of_species')

freq_table
