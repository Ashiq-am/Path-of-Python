# import modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Reading the dataset
data = pd.read_csv('Dataset.csv')
print("The shape of the dataframe is: ",data.shape)
