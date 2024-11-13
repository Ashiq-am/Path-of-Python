# import packages and libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading the csv file
data = pd.read_csv('headbrain3.csv')

sns.residplot(x='Head_size', y='Brain_weight', data=data)

plt.show()
