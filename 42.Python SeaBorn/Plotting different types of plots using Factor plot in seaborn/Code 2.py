# importing required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Pokemon.csv')

# Type 1 v / s Attack violin plot
sns.factorplot(x ='Type 1', y ='Attack',
			kind = 'violin', data = df)

# show the plots
plt.show()
