# import library & dataset
import seaborn as sns


tips = sns.load_dataset("tips")
ax = sns.boxplot(data=tips, orient="h", palette="Set2")
