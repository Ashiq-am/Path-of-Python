# importing library
import seaborn as sns
import matplotlib.pyplot as plt
# loading seaborn dataset tips
tdata = sns.load_dataset('tips')

tdata = tdata.head(20)
# creating boxplot
sns.boxplot(x='size', y='tip', data=tdata)

# adding data points
sns.stripplot(x='size', y='tip', data=tdata, color="black", size=8, alpha=0.5)
# display plot
plt.show()
