import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
