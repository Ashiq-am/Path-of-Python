import seaborn as sns
import matplotlib.pyplot as plt

dots = sns.load_dataset("dots")
hue_order = ["low", "medium", "high"]
sns.lineplot(data=dots, x="time", y="firing_rate", hue="coherence", hue_order=hue_order)
plt.title("Lineplot with hue_order")
plt.show()
