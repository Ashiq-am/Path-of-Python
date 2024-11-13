# Barplot with wider error bars
sns.barplot(x='Category', y='Values', data=data, yerr=np.mean(errors), errwidth=2) # Use np.mean to get a single value for errors
plt.show()
