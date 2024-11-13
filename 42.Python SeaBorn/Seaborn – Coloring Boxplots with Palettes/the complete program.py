# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load datset
ds = sns.load_dataset("tips")

plt.figure(figsize=(8, 6))

# use palette method
ax = sns.boxplot(data=ds, orient="h", palette="Set1")
