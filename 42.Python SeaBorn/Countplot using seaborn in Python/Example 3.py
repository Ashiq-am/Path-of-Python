# importing the required library

import seaborn as sns
import matplotlib.pyplot as plt

# read a tips.csv file from seaborn libraray
df = sns.load_dataset('tips')

# count plot along y axis
sns.countplot(y ='sex', hue = "smoker", data = df)

# Show the plot
plt.show()
