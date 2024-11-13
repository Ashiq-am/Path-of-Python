import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

sns.violinplot(x="day", y="total_bill", data=tips, width=0.5)
plt.show()
