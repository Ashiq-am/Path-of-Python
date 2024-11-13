# importing libraries
import seaborn as sns
import matplotlib.pyplot as plt

# loading diamonds dataset provided by seaborn
diam = sns.load_dataset('diamonds')

# making ECDF plot using displot() on table
# column on the basis of cut of diamond
# setting up the color of plot by setting
# up the palette to icefire_r
sns.displot(data=diam,x='table',kind='ecdf',hue='cut',palette='icefire_r')

# visualizing the plot using matplotlib.pyplot
# show() function
plt.show()
