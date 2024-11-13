fig = plt.gcf()  # Get the current figure
fig.set_size_inches(18, 8)  # Set the size in inches
sns.heatmap(df)
plt.show()
