# Importing libraries for dataframe creation
# and graph plotting
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating our own dataframe
data = {"Name": ["Alex", "Bob", "Clarein", "Dexter"],
		"Marks": [45, 23, 78, 65]}

# Now convert this dictionary type data into a pandas dataframe
# specifying what are the column names
df = pd.DataFrame(data, columns=['Name', 'Marks'])
