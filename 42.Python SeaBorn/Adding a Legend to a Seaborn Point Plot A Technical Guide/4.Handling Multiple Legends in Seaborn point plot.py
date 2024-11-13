import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating multiple point plots
sns.pointplot(x="day", y="total_bill", hue="sex", data=tips, markers=["o", "s"], linestyles=["-", "--"])
sns.pointplot(x="day", y="tip", hue="sex", data=tips, markers=["x", "^"], linestyles=[":", "-."])

# Customizing the legend
plt.legend(title='Legend', loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
