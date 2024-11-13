# importing the required library

import seaborn as sns
import matplotlib.pyplot as plt

# read a tips.csv file from seaborn libraray
df = sns.load_dataset('tips')

# count plot on single categorical variable
sns.countplot(x ='sex', data = df)

# Show the plot
plt.show()
