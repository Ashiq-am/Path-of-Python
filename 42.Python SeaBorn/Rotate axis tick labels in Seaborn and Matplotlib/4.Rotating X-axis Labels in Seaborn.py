import seaborn as sns
import matplotlib.pyplot as plt

g = sns.barplot(x=["Asia", "Africa", "Antartica", "Europe"],
				y=[90, 30, 60, 10])
g.set_xticklabels(
	labels=["Asia", "Africa", "Antartica", "Europe"], rotation=30)
# Show the plot
plt.show()
