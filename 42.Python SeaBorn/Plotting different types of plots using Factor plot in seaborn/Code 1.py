# importing required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Pokemon.csv')

# Stage v / s Attack point plot
sns.factorplot(x ='Stage', y ='Attack', data = df)
sns.factorplot(x ='Stage', y ='Defense', data = df)

# Show the plots
plt.show()
