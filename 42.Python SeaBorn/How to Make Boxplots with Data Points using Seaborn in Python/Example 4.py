# importing library
import seaborn as sns
import matplotlib.pyplot as plt
# loading seaborn dataset tips
tdata = sns.load_dataset('tips')

tdata = tdata.head(10)
# creating boxplot
sns.boxplot(x='size', y='tip', data=tdata)

# adding data points
sns.stripplot(x='size', y='tip', data=tdata, color="grey", size=8)
# display plot
plt.show()
