import seaborn as sns

tips = sns.load_dataset("tips")

sns.jointplot(data=tips, x="total_bill", y="tip", hue="time")
