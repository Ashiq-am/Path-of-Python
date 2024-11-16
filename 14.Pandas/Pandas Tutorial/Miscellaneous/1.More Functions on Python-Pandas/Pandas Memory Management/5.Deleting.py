# importing the modules
import pandas as pd
import numpy

# Reading the csv file
df = pd.read_csv('data.csv')

# Deleting unwanted columns
del df["Unnamed: 0"]
