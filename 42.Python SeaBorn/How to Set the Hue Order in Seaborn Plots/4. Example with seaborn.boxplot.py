import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
order = ["Sun", "Sat", "Fri", "Thur"]
hue_order = ["Male", "Female"]

# Plot with order and hue_order
sns.boxplot(x="day", y="total_bill", hue="sex", data=data, order=order, hue_order=hue_order)
plt.title("Boxplot with order and hue_order")
plt.show()
