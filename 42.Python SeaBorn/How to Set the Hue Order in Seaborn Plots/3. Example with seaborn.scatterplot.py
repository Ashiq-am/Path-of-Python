import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
hue_order = ["Yes", "No"]
sns.scatterplot(data=data, x="total_bill", y="tip", hue="smoker", hue_order=hue_order)
plt.title("Scatterplot with hue_order")
plt.show()
