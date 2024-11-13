# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("tips")

# draw lineplot
# hue by sex
# style to hue
sns.lineplot(x="total_bill", y="size",
			hue="sex", style="sex",
			data=data)

plt.show()
