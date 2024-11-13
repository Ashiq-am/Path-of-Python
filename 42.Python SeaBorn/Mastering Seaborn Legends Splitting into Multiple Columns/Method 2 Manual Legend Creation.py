import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample plot
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)

# Manually create the legend
legend_handles, legend_labels = ax.get_legend_handles_labels()
plt.legend(legend_handles, legend_labels, ncol=2, title="Sex")

plt.show()
