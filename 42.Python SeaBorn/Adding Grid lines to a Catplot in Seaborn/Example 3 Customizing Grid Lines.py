import seaborn as sns
import matplotlib.pyplot as plt

exercise = sns.load_dataset("exercise")
g = sns.catplot(x="time", y="pulse", hue="kind", col="diet", data=exercise)

# Customize grid lines
for ax in g.axes.flat:
    ax.grid(True, color='r', linestyle='--', linewidth=0.5)
plt.show()
