import seaborn as sns
import matplotlib.pyplot as plt

g = sns.barplot(x=["Asia", "Africa", "Antartica", "Europe"],
				y=[90, 30, 60, 10])

g.set_yticklabels(labels=[0, 20, 40, 60, 80], rotation=30)

# Show the plot
plt.show()
