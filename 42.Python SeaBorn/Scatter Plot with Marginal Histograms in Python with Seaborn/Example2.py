import seaborn as sns

tips = sns.load_dataset("tips")

# here "*" is used as a marker for scatterplot
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", marker="*")
