# importing required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Pokemon.csv')

# Stage v / s count - count plot
sns.factorplot(x ='Stage', kind = 'count', data = df)

# show the plots
plt.show()
