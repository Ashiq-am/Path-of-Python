# import required module
import seaborn as sns

# assign required values
_, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

# illustrate count plots
sns.countplot(x='Outcome', data=diabetes, ax=axes[0])
sns.countplot(x='BloodPressure', data=diabetes, ax=axes[1])
