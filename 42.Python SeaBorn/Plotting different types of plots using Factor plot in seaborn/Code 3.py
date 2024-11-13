# importing required library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read a csv file
df = pd.read_csv('Pokemon.csv')

# Type 1 v / s Defense bar plot
# with Stage column is used for
# colour encoding i.e
# on the basis of Stages different
# colours is decided, here in this
# dataset, 3 Stage is mention so
# 3 different colours is used.
sns.factorplot(x ='Type 1', y ='Defense',
			kind = 'bar', hue = 'Stage',
			data = df)

# show the plots
plt.show()
