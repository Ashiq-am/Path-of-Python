# importing and creating alias for seaborn
import seaborn as sns

# loading tips dataset
tips = sns.load_dataset("tips")

# plotting scatterplot with histograms for features total bill and tip.
sns.jointplot(data=tips, x="total_bill", y="tip")
