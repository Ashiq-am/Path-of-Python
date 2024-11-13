import seaborn as sns
import pandas as pd


datasets = sns.load_dataset('iris')

datasets.head()
sns.violinplot(x='species', y='petal_length', data=datasets,
			inner="quart", linewidth=1)
