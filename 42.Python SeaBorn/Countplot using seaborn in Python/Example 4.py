# importing the required library

import seaborn as sns
import matplotlib.pyplot as plt

# read a tips.csv file from seaborn libraray
df = sns.load_dataset('tips')

# use a different colour palette in count plot
sns.countplot(x ='sex', data = df, palette = "Set2")

# Show the plot
plt.show()
