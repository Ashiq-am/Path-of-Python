import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample plot
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)

# Split the legend into two columns
leg = ax.legend()
leg.set_title("Sex")
leg._ncol = 2

plt.show()
