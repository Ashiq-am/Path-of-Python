import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

# Create histogram with log-scaled x-axis (base 2)
sns.histplot(tips["total_bill"].apply(lambda x: 2**x), bins=20, log_scale=(True,False))
plt.xlabel("Log Total Bill (base 2)")
plt.ylabel("Frequency")
plt.show()
