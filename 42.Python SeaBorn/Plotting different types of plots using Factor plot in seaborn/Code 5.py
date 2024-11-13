# importing required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Pokemon.csv')

# Stage v / s Defense strip plot
sns.factorplot(x ='Stage', y ='Defense',
			kind = 'strip', data = df)

# show the plots
plt.show()
